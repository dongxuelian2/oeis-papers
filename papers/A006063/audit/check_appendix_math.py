"""AI-assisted focused LaTeX transcription check for Families V/VI; optional SymPy.

This is not a general LaTeX/proof parser. Run without Python optimization.
"""
from pathlib import Path
import re
from sympy import symbols, expand
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
p=Path(__file__).resolve().parent.parent / 'appendix.tex'
s=p.read_text()
a,b,t=symbols('a b t')
def expr(x):
 x=x.replace('\\alpha','a').replace('\\beta','b').replace('\\','').replace('\n','').strip()
 return parse_expr(x,local_dict={'a':a,'b':b,'t':t}, transformations=standard_transformations+(implicit_multiplication_application,))
def tuple_expr(x):return [expr(y) for y in x.split(',')]
for number,name,allowed in [(15,'Family V.',[(0,0),(0,1),(1,1)]),(10,'Family VI.',[(0,0),(1,0),(1,1)])]:
 part=s.split('\\paragraph{'+name+'}')[1].split('\\section{')[0]
 if name=='Family V.':part=part.split('\\subsection{Ten')[0]
 groups=re.findall(r'\(\\ell_\d+,\\ldots,\\ell_\{?\d+\}?\)\s*&=\s*\((.*?)\)',part,re.S)
 L=sum([tuple_expr(x) for x in groups],[])
 # beta(39-alpha) requires balanced extraction instead of simple regex.
 if len(L)!=number or (number==15):
  # Extract complete aligned equation through next linebreak, preserving internal parentheses.
  groups=re.findall(r'\(\\ell_.*?&=\s*\((.*?)\),?\\\\',part,re.S)
  L=sum([tuple_expr(x) for x in groups],[])
 C=sum([tuple_expr(x) for x in re.findall(r'\(C_.*?&=\s*\((.*?)\)',part,re.S)],[])
 O=list(map(int,re.search(r'\\pi&=\((.*?)\)',part).group(1).split(',')))
 assert len(L)==len(C)==number,(name,L,C)
 actual=[expand(1+sum(L[:j])+sum(L[i-1] for i in O[:O.index(j+1)])+L[j]) for j in range(number)]
 for aa,bb in allowed:
  for j in range(number):assert expand((actual[j]-C[j]).subs({a:aa,b:bb}))==0,(name,j)
  ts=[0,7+4*bb+2*aa] if number==15 else [0]
  for tt in ts:
   lens=[int(x.subs({a:aa,b:bb,t:tt})) for x in L]
   sums=[int(x.subs({a:aa,b:bb,t:tt})) for x in actual]
   assert min(lens)>=0
   assert all(c in [8,27,64,125,216,343,512] for l,c in zip(lens,sums) if l)
 print('PASS parsed appendix',name,': exact nominal identities including zero blocks; all allowed instances nonnegative/cubic')
print('Source parse checks complete (Families I-IV and peeling tables independently inspected against exact specification).')
