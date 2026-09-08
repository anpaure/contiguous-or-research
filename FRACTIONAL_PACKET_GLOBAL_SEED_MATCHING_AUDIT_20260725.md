# Independent audit of the global suspended-seed matching

Date: 2026-07-25

Audited file: FRACTIONAL_PACKET_GLOBAL_SEED_MATCHING_20260725.md.

## Verdict

**PASS.** The primitive-component language, recursive disjointness,
generating function, singular constant, edit-robust inequality, and parity
transversal are correct.

Two further exact consequences were independently proved:

1. a native \((2\ 3)\)-component cover of all recursive triples costs at
   least
   \[
   \left(
   \frac{275}{19321}+\frac{6528}{1238769}+o(1)
   \right)\operatorname{Cat}_m;
   \]
2. every exact child in the entire canonical \((2\ 3)\)-interaction cube
   still has packet mass at least
   \[
   \left(
   \frac{107897}{19784704}+o(1)
   \right)\operatorname{Cat}_m
   \]
   from transposition-invariant mixed triples.

Full proofs of the two extensions are in Sections 8--9 of
FRACTIONAL_PACKET_PREFIX_SUSPENSION_OBSTRUCTION_AUDIT_20260725.md.

## 1. Recursive language

With \(A,B\) the two primitive semilength-four seed roots and \(D=1100\),
the third alternative is \(DD\). A clean prefix avoids
\(A,B,DD\) and does not end in \(D\). If

\[
 E(z)=zC(z)-z^2-2z^4,
\]

then clean prefixes have generating function

\[
 U_0(z)=\frac1{1-(1+z^2)E(z)}.
\]

The first active occurrence decodes every clean-stage triple. The only
unused active roots begin uniquely with \(UDA\) or \(UDB\), with \(U\)
clean. These dirty prefixes are prefix-free and have series
\(2z^6U_0\), so recursion in their suffixes is disjoint. Hence

\[
 M(z)
 =z^4U_0C+2z^6U_0M
 =
 \frac{z^4C}
 {1-(1+z^2)(zC-z^2-2z^4)-2z^6}.
\]

This verifies the main exact generating function.

## 2. Singular constant

For \(s=\sqrt{1-4z}\),

\[
 zC(z)=\frac{1-s}{2}.
\]

The matching denominator is

\[
 \frac{139}{256}+\frac{17}{32}s+O(s^2).
\]

Its subtracted nonnegative series has value \(117/256<1\) at \(z=1/4\),
so no smaller-modulus pole occurs. Comparing square-root coefficients with
\(C(z)\) gives

\[
 \frac{[z^m]M(z)}{\operatorname{Cat}_m}
 \to
 \frac1{256}
 \left[
 \frac{256}{139}
 +\frac{17}{32}\left(\frac{256}{139}\right)^2
 \right]
 =
 \frac{275}{19321}.
\]

The edit-robust bound follows because the owner triples are disjoint: one
removed canonical row hits at most one triple.

The reported repaired-factor difference is also correct:

\[
 \frac{275}{19321}-\frac1{128}
 =\frac{15879}{2473088}.
\]

## 3. Parity transversal

The number of \(A\)-components in the three variants is \(k+1,k,k\).
Thus roots with odd \(A\)-count meet every local triple. Reweighting \(A\)
by \(-1\) gives

\[
 C_-(z)=\frac{C(z)}{1+2z^4C(z)}.
\]

The odd class has series \((C-C_-)/2\), and its normalized limit is

\[
 \frac12\left(1-\left(\frac{64}{65}\right)^2\right)
 =\frac{129}{8450}.
\]

Therefore the audited full-hypergraph bracket is

\[
 \frac{275}{19321}
 \le
 \liminf\frac{\tau_{\rm seed}(m)}{\operatorname{Cat}_m}
 \le
 \limsup\frac{\tau_{\rm seed}(m)}{\operatorname{Cat}_m}
 \le
 \frac{129}{8450}.
\]

## 4. Scope

The theorem is a global positive-density edit obstruction around the
canonical factor, not a proof that every exact factor contains this seed.
The invariant mixed-seed extension does, however, rule out every factor in
the canonical \((2\ 3)\)-interaction cube as an \((\mathrm{FSP}_A)\)
candidate.
