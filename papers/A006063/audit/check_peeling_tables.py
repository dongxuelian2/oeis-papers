"""AI-assisted independent check of the printed peeling batches; standard library."""
C=[k**3 for k in range(2,8)]
for n in range(173,182):
 V=set(range(1,n+1)); rounds=[[(i,216) for i in range(125,343-n)],[(i,64) for i in range(34,216-n)],[(i,216) for i in range(95,277-n)]]
 if n==173:
  rounds += [[(i,8) for i in [4,5]]+[(i,27) for i in range(8,13)],[(i,216) for i in [45,46,106,107,108,122]],[(31,64),(172,216),(173,216)]]
  rounds += [[x] for x in zip([92,1,20,111,13,104,6,123,32],[216,8,125,125,125,125,8,216,64])]
 if n in [174,175]:
  rounds += [[(4,8)]+[(i,27) for i in range(8,12)] if n==174 else [(i,27) for i in range(8,11)],[(i,216) for i in [45,46,47,106,107,108]],[(15,27)]+[(i,216) for i in [172,173,174]]]
  rounds += [[x] for x in zip([113,22,3,94,33,124,7,105,14,112,21,2,93],[216,27,125,125,125,125,27,216,27,216,27,125,125])]
 for r in rounds:
  # Test the whole batch before removing anything in the batch.
  for i,c in r: assert i in V and {q-i for q in C if q-i in V}=={c-i},(n,i,c)
  V-={x for i,c in r for x in [i,c-i]}
 if n in [173,174]: assert not V
 if n==175: assert V=={4,11,16,23,41,48,102,114,168,175}
 print('PASS stated simultaneous peeling batches n=',n,'remaining=',len(V))
