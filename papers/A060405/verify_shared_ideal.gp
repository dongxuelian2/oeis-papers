\p 80

{
  my(field_a = x^4 - 2*x^2 - 4,
     field_b = x^4 - 4*x^2 + 2,
     product_polynomial, defining, expected, bnf);
  product_polynomial = subst(polresultant(y^2 - 2,
    x^2 - 2*(2+y)*x - 4*(2+y)^2, y), x, x^2);
  defining = [field_a, field_b, product_polynomial,
    polcompositum(field_a, field_b)[1]];
  expected = [[2,1], [4,0], [4,2], [8,4]];
  for(i = 1, #defining,
    bnf = bnfinit(polredabs(defining[i]), 1);
    if(bnf.nf.sign != expected[i] || bnf.no != 1 || !bnfcertify(bnf),
      print("Class number certification failed for field ", i); quit(1)));
  print("Certified class number one for L_A, L_B, F and E.");
}

{
  my(pol = x^4 - 14*x^2 + 9, nf = nfinit(pol), t = Mod(x,pol),
     s = (t-3/t)/2, alpha = (2+t+3/t)/4, z = alpha*(1+s),
     prime2 = idealprimedec(nf,2)[1], primes3 = idealprimedec(nf,3),
     f, h2, h3, result, excluded = []);
  forstep(j = 1, 11, 2,
    f = z^j-s;
    h2 = nfhilbert(nf,f,2*alpha,prime2);
    h3 = prod(i = 1,#primes3,nfhilbert(nf,f,2*alpha,primes3[i]));
    if(h2 != if(j%3 == 2,-1,1) || h3 != if(j%4 == 1,-1,1),
      print("Unexpected local symbol for j = ", j); quit(1));
    result = -h2*h3;
    if(result == -1, excluded = concat(excluded,3*j)));
  if(excluded != [9,15,21], print("Unexpected excluded classes"); quit(1));
  print("Verified classes excluded modulo 36: ", excluded);
}

quit
