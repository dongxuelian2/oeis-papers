# A whole-block Jacobi certificate beyond the 3-adic sieve

This criterion certifies that every rotation in a given endpoint block is an integer nonpower, even when every rotation is a square over Q_3. It uses a quadratic character of the whole cyclic modulus, without factoring that modulus. It is still a modular obstruction, not a theorem that all local methods have been bypassed, and it does not settle Kashihara's conjecture.

## Theorem

Let W_m be the decimal concatenation of 1,...,m, let D=D(m) be its digit length, and put

    Delta=10^D-1,
    R_(m,k)=10^(D(k))W_m-Delta W_k,       0<=k<m.

Assume D>=3 and

    a=v_3(Delta)=2+v_3(D)>=3,
    v_3(W_m)=2,
    z=W_m/9=1 modulo3.

Set M=Delta/3^a. If the Jacobi symbol (z/M) equals -1, then EVERY R_(m,k) is not a nontrivial integer perfect power.

At the same time every rotation is a square in Q_3, and the greatest common divisor of all rotations is exactly 9. Thus the certificate is not merely the existing 3-adic nonpower test or a common valuation-one prime obstruction.

## Proof

The identity v_3(10^D-1)=2+v_3(D) is LTE. In the rotation identity, the first term has valuation 2 at 3, while the second is divisible by 3^a with a>=3. Hence v_3(R_(m,k))=2. Moreover R_(m,k)/9=z modulo3, so every normalized unit is 1 modulo3. The usual local square criterion proves that each rotation is a square in Q_3.

If an integer rotation were a nontrivial perfect power, a prime divisor ell of its exponent would divide its 3-adic valuation 2. Therefore ell=2, so it would be an integer square. It suffices to rule out squares.

For D>=3, Delta=7 modulo8 and Delta=4 modulo5. Quadratic reciprocity and the supplementary law give

    (10/Delta)=(2/Delta)(5/Delta)=1*1=1.

The Jacobi symbol is defined because Delta is odd and coprime to10. Since (10/3)=1 and Delta=3^a M, multiplicativity in the denominator gives (10/M)=1.

Dividing the rotation identity by9 is legitimate, and Delta/9=3^(a-2)M. Thus

    R_(m,k)/9 = 10^(D(k)) z modulo M.

Its Jacobi symbol modulo M is consequently (10/M)^(D(k))(z/M)=-1. An integer square has Jacobi symbol 0 or 1 for every odd positive denominator, so R_(m,k)/9 cannot be an integer square. Since v_3(R_(m,k))=2, an integer square R_(m,k) would have R_(m,k)/9 equal to an integer square. This contradiction proves the claim.

Finally (z/M)=-1 implies gcd(z,M)=1, and z is coprime to3. Therefore gcd(W_m,Delta)=9. The gcd of all rotations is precisely gcd(W_m,Delta): this number divides each rotation; conversely the first two cuts give W_m and 10W_m-Delta, whose gcd is gcd(W_m,Delta). This proves the final assertion.

## Ten explicit certificates

The accompanying exact script verifies the theorem's hypotheses at the following endpoints:

    5040, 5067, 5094, 5121, 5175,
    5202, 5229, 5283, 5337, 5391.

For all of them D=4m-1107 and a=4. The normalized unit is 1 modulo3 and the Jacobi symbol is -1. The theorem therefore certifies all 51,939 rotations in these ten blocks. These endpoints lie beyond the previously recorded search through endpoint 5000; no claim about priority or exhaustive coverage of the intervening endpoints is made.

The exact certificate contains endpoint indices, digit lengths, valuations, normalized residues and Jacobi results. The large integer prefixes and moduli are reconstructed deterministically rather than embedded as enormous decimal strings. No factorization of 10^D-1 is used.

## Verification and interpretation

Run:

    python verify_cyclic_jacobi_certificate.py

The script constructs exact prefixes, checks every displayed hypothesis, and tests five selected cuts per block against the claimed invariant. If SymPy is installed, it also independently cross-checks the Jacobi calculation with SymPy. The full-block conclusion is a proof consequence, not a claim that the script individually tested all 51,939 rotations for perfect powers. The selected-cut tests and optional library cross-check are reported separately.

This is a sufficient certificate, not an equivalent classification. A zero or positive Jacobi symbol does not imply that a rotation is an integer power or that the conjecture fails. The ten endpoints do not establish an infinite progression of successful certificates.

The criterion is compatible with the growing-prime local survivor theorem: its modulus can contain primes far beyond a prescribed small-prime cutoff. It supplies a practical whole-block test with a different modulus, not a resolution of every remaining endpoint. The main manuscript and PDF are unchanged.
