# Jacobi block certificates with power-of-two valuations

This supplement extends the cyclic Jacobi criterion to a larger class of exact 3-adic valuations and records a complete scan of its hypotheses on a finite endpoint interval. It does not infer an infinite family or success rate from that scan.

## Generalized sufficient criterion

Use W_m, D(m), Delta=10^(D(m))-1 and R_(m,k) as in CYCLIC_JACOBI_CERTIFICATE.md. Assume D(m)>=3 and

    b=v_3(W_m)=2^r for an integer r>=1,
    a=v_3(Delta)=2+v_3(D(m))>b,
    z=W_m/3^b=1 modulo3.

Put M=Delta/3^a. If the Jacobi symbol (z/M) is -1, then every rotation R_(m,k) is an integer nonpower. Every rotation is nevertheless a square in Q_3, and the gcd of the block is exactly 3^b.

## Proof

The rotation identity gives v_3(R_(m,k))=b, because the first term has valuation b and the second has valuation at least a>b. Its normalized unit is z modulo3. Since b is even and z=1 modulo3, every rotation is a 3-adic square.

If a positive rotation were a nontrivial integer power, a prime divisor of its exponent would divide b=2^r, and hence would be 2. The rotation would therefore be an integer square. Because b is even, dividing that square by 3^b would still give an integer square.

As proved in the original Jacobi supplement, (10/M)=1 for this modulus. Also

    R_(m,k)/3^b = 10^(D(k)) z modulo M,

because Delta/3^b is an integer multiple of M. Thus its Jacobi symbol is -1, contradicting its being an integer square. This rules out every integer power exponent, not just exponent b.

Finally (z/M)=-1 implies gcd(z,M)=1. With v_3(W_m)=b<a, this gives gcd(W_m,Delta)=3^b. The first two cuts show that this is also the gcd of the entire block. All steps are exact; no factorization of Delta is needed.

The previously published criterion is the case b=2. The extension also applies to b=4,8,16,... whenever all its hypotheses are verified. A positive even valuation with an odd prime divisor is not covered by this argument.

## Finite endpoint scan and its scope

The script `verify_jacobi_endpoint_range.py` scans every endpoint m from 5001 through 10000. It tests whether b is a power of two at least 2, a>b and the normalized unit is 1 modulo3. For every endpoint meeting these preliminary conditions it computes the exact Jacobi symbol. Successful certificates are stored individually in `jacobi-endpoint-range-certificate.json`; the corresponding output reports the counts.

The completed scan gives 206 endpoints meeting the preliminary conditions: 94 have Jacobi symbol -1, 11 have symbol 0 and 101 have symbol +1. The 94 certified blocks comprise 84 valuation-2 blocks and 10 valuation-4 blocks, covering 706,590 rotations by the theorem. The ten earlier blocks, covering 51,939 rotations, are included; the extension therefore adds 84 blocks and 654,651 certified rotations. The recorded run also passes 188 selected-cut checks and 206 optional SymPy symbol cross-checks.

For each successful block the script additionally checks the first nonzero cut and the last cut. When SymPy is installed, every computed preliminary Jacobi symbol is cross-checked with SymPy. It does not test each rotation individually for being a perfect power: whole-block exclusion is the consequence of the proved invariant. It does not classify endpoints where the hypotheses fail or the symbol is zero or positive.

Run next to the previously published verifier:

    python verify_jacobi_endpoint_range.py

That script imports the exact integer Jacobi routine and valuation routine from `verify_cyclic_jacobi_certificate.py`. The optional SymPy cross-check is reported separately from the reproducible core calculation.

The ten previously published blocks lie inside this scan and are included in its totals, not counted again as additional blocks. In particular the new valuation-4 certificates are outside the scope of the earlier valuation-2 formulation. Neither the counts nor their apparent spacing is evidence of an infinite arithmetic progression.

## Infinite-family investigation

A natural attempt uses a fixed factor 37 of the cyclic modulus and the existing formula W_m=m(m+1)/2+11d modulo37 when 3 divides the digit width d. Combined with the 3-adic criterion, it yields explicit congruence families. However the main manuscript already contains this type of 37-character whole-block exclusion. Such a recombination is not claimed here as a new infinite-family theorem.

No infinite progression of negative signs for the full cyclic Jacobi modulus has been proved in this supplement. Kashihara's full conjecture remains open. The original manuscript and PDF are unchanged.
