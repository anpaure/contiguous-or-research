# Clean-room audit of the monotone-rotor labelled lift

Date: 2026-08-01  
Lane: R  
Objects audited: `MATH_CANDIDATE_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`
and its corrected promotion
`MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`  
Verdict: **PASS after scope and notation corrections stated below.**

The age-type circulation in the candidate really does lift to a literal
fractional de Bruijn circulation.  The lift is exact for the invariant,
rank-only marked-trace polytope.  Clearing denominators gives an integer
Eulerian **multicover**, not one selected occurrence per owner.  Thus the
candidate closes the invariant fractional trace gate but does not close the
integral owner/target rotor-fusion gate.

The promoted theorem has the corrected ambient-`k` notation and parameter
range, and its Lemma 2.1 agrees with the explicit degree calculation below.
In its denominator sentence, rational marked-target integrality should be
read as requiring both rational `f` and rational mark splits; rational `f`
alone clears only the unmarked trace multigraph.

## 1. Correct parameter scope

The nontrivial statement should be written with

\[
                 k\ge r\ge2,\qquad 1\le d\le r-1,
\]

and with `ST_(k,r,d)`, not `ST_(r,d)`, if one uses the notation of
`MATH_THEOREM_TRIANGULAR_MARKED_TRACE_CIRCULATION_AND_K6_BALANCED_CLOCK_20260801.md`.
The construction is uniform in `k`, which is why suppressing `k` is
conceptually harmless, but the literal polytope itself was defined with `k`.
The cases with `d=0` are empty/trivial and should be separated.

## 2. Exact biregular degrees

Fix an owner \(T\), \(|T|=r\), and a type
\(c=(c_0,\ldots,c_d)\), with \(c_0>0\), \(c_i\ge0\), and
\(\sum_i c_i=r\).  Let

\[
 \mathcal P_c(T)=\{(C_0,\ldots,C_d):
 T=C_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_d,
 |C_i|=c_i\}.
\]

Then

\[
                         N_c:=|\mathcal P_c(T)|
                         ={r!\over\prod_{i=0}^d c_i!}.                 \tag{2.1}
\]

For types \(c,c'\), join \(P=(C_i)\) to \(P'=(C'_i)\) when

\[
                         C'_{i+1}\subseteq C_i\quad(0\le i<d).        \tag{2.2}
\]

This relation is nonempty exactly when

\[
                         c'_{i+1}\le c_i\quad(0\le i<d).              \tag{2.3}
\]

For a fixed source its degree is

\[
 D^+_{c,c'}=\prod_{i=0}^{d-1}{c_i\choose c'_{i+1}}.                  \tag{2.4}
\]

For a fixed target, put \(e_i=c_i-c'_{i+1}\).  The elements of
\(C'_0\) are distributed among the old cells with residual sizes
\(e_0,\ldots,e_{d-1},c_d\), so the fixed-target degree is

\[
 D^-_{c,c'}={c'_0!\over c_d!\prod_{i=0}^{d-1}e_i!}.                  \tag{2.5}
\]

Direct cancellation gives

\[
 E_{c,c'}:=N_cD^+_{c,c'}=N_{c'}D^-_{c,c'}.                           \tag{2.6}
\]

This proves biregularity without appealing only to group transitivity.

## 3. Lift of a type circulation

Let \(f(c,c')\ge0\) be supported on (2.3), with

\[
 \sum_{c'}f(c,c')=\sum_{c'}f(c',c)=\pi(c),\qquad
 \sum_c\pi(c)=1.                                                     \tag{3.1}
\]

Give each labelled arc in the \((c,c')\)-relation weight

\[
                         {f(c,c')\over E_{c,c'}}.                     \tag{3.2}
\]

At every source partition of type \(c\), the contribution of this type
edge is \(f(c,c')/N_c\).  At every target partition of type \(c'\), it is
\(f(c,c')/N_{c'}\).  Summing (3.2) over adjacent types and using (3.1)
therefore gives equal incoming and outgoing weight

\[
                         {\pi(c)\over N_c}                            \tag{3.3}
\]

at every labelled partition of type \(c\).  Thus the lift is a conserved
literal labelled flow, and the claimed uniformity coefficients are exact.

Conversely, projecting any stationary literal flow to its age types gives
(2.3) and (3.1).  Hence this is a necessity-and-sufficiency statement on the
invariant rank-only fractional quotient, not merely a sufficient averaging
device.

## 4. Literal word reconstruction

For a labelled arc \(P\to P'\), the partition identities and (2.2) imply

\[
 C'_0=C_d\ \cup\!
       \bigcup_{i=0}^{d-1}(C_i\setminus C'_{i+1}),                   \tag{4.1}
\]

as a disjoint union.  Emit the letter \(B_{t+1}=C'_{0}\).  It is nonempty
because every allowed target type has \(c'_0>0\).  Equation (4.1) says
precisely that retained coordinates age by one and all other coordinates
are refreshed.  Every finite nonnegative conserved labelled flow is a
nonnegative sum of directed cycles (with real coefficients allowed).
Therefore each directed labelled-partition cycle emits a periodic literal
word in which every \((d+1)\)-window has owner exactly \(T\), and summing
those word circulations realizes the original flow.

At a state \(P=(C_0,\ldots,C_d)\), the union of the last \(j\) letters is

\[
                         C_0\cup\cdots\cup C_{j-1}.                  \tag{4.2}
\]

Consequently its rank is the advertised partial sum
\(s_j(c)=c_0+\cdots+c_{j-1}\).  This verifies the literal suffix labels,
not only their cardinalities.

Uniform measure on \(\mathcal P_c(T)\) makes a cumulative cell of rank \(s\)
uniform on \({T\choose s}\).  Repeating the construction for every named
owner and symmetrizing gives, for a fixed rank-\(s\) target, load

\[
 { {k-s\choose r-s}\over {r\choose s}}q_s
       ={ {k\choose r}\over {k\choose s}}q_s.                       \tag{4.3}
\]

Thus the target-load coefficient in the candidate is correct.

## 5. Marks and occurrence scope

If an age class is empty, two partial sums may agree and represent the same
literal suffix set.  The correct availability object is therefore the set
of distinct ranks \(R(c)\), as in the earlier quotient audit.  All three
rotor families used in the candidate have positive age classes, so their
marked suffixes are strictly nested and no multiplicity error occurs.

For a general lifted type distribution, rank marks are splittable mass.
The constraints

\[
 0\le m_s(c)\le\pi(c){\bf1}_{s\in R(c)}
\]

have no cross-rank sum constraint because several distinct suffixes of one
trace atom may be marked together.  They can be realized, for example, by
independently marking the available ranks after splitting the mass of each
type.  This is still fractional occurrence semantics.

It does **not** imply any of the following:

* one trace edge selected for each named owner;
* one occurrence selected for each named lower target;
* injective common-cap/compiler assignment;
* Johnson transitions between different owners;
* connected or rooted support; or
* preservation of guarded upper witnesses.

Those constraints destroy the transitivity/biregularity used above.

## 6. Denominators and integrality

If \(f\) and the mark splits are rational, choose a common denominator
divisible by every denominator of

\[
                         f(c,c')/E_{c,c'}                            \tag{6.1}
\]

and of every mark split.  Multiplication by that denominator produces an
integer conserved multigraph on labelled partitions.  It decomposes into
directed cycles and hence into finitely many periodic literal words.

This is an **integer multicover**: a fixed owner generally occurs many
times.  Division by the common denominator is essential to recover owner
mass one.  No one-copy factor or integral compiler follows.  For an
arbitrary real point of the monotone polytope there need not even be a finite
denominator; for the triangular Ferrers vector all data are rational, so a
finite multicover does exist.

## 7. Rotor coefficients and the O3 audit

The source
`scratch/audit_monotone_rotor_fractional_clock_20260801.cpp` correctly
checks:

1. legality of the short self-loop type;
2. legality of every long-rotor and mixed-rotor type edge in its tested
   range; and
3. the exact integer identities giving long marginal \(d/b\) and mixed
   marginal \((d-a)/(b-a)\).

Its source SHA-256 at audit time is

```text
a45647bc0d8756c9cba998a9364cebc6c5f000ad6fff25852f531dd747da57e6
```

The program tests `3<=r<=28`, `d<=8`, and `b<=17`.  It does not check the
labelled biregular lift, the convex-hull proof, or the Ferrers application;
Sections 2--6 above provide the independent proofs of those steps.  No
solver or finite-search evidence is used in this verdict.

## 8. Ferrers-boundary application

Take \(r=\lceil k/2\rceil\), \(W={k\choose r}\), and extend \(b_s=0\)
for \(s>d\).  For a standard left-filled triangular Ferrers board,

\[
 b_1\ge b_2\ge\cdots\ge b_d\ge0.                                   \tag{8.1}
\]

Moreover \(b_s\le d-s+1\le d\le r-1\), so \(b_s\le{k\choose s}\).
Central unimodality gives \({k\choose s}\le W\) for \(s<r\).  Hence

\[
                         0\le q_s={{k\choose s}-b_s\over W}\le1.    \tag{8.2}
\]

For \(1\le s<r-1\),

\[
 q_{s+1}-q_s=
 { {k\choose{s+1}}-{k\choose s}+b_s-b_{s+1}\over W}\ge0.          \tag{8.3}
\]

Finally, with \(h=\sum_sb_s=(\Lambda-dW)_+\),

\[
                         \sum_{s=1}^{r-1}q_s
                         ={\Lambda-h\over W}\le d.                  \tag{8.4}
\]

Thus the actual Ferrers vector belongs to the monotone demand polytope.
Combined with the rotor clocks, it lies in `ST_(k,r,d)`.

This conclusion is unconditional at the invariant fractional trace level.
The exact remaining gate is the integral, occurrence-labelled owner/target
rotor fusion, together with its physical guards and compiler cap.
