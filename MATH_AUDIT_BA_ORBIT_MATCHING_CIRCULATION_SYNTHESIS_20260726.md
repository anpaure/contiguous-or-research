# Audit of the \(BA\)-orbit parity and first-annulus synthesis

Date: 2026-07-26

Audited file:
MATH_THEOREM_BA_ORBIT_MATCHING_CIRCULATION_PARITY_AND_ANNULUS_NOGO_20260726.md.

Method: direct coordinate-footprint verification and comparison with the
canonical nested-star packet theorem. No computation or external input.

## 0. Verdict

The two claims which close the strict alternating architecture are
correct:

1. for even \(m\), every activated \(BA\)-orbit has an even owner
   incidence vector and no nonzero capacity-one activation is possible;
2. for odd \(m\ge3\), every owner-simple alternating component has
   factor-two collision at lower depth \(q=1\), giving exactly
   \[
   M_1^-\ge
   \binom{2m+1}{m-1}-\frac G2
   =
   \frac{m-2}{2(m+2)}W+\frac{W-G}{2}.
   \]

The packet obstruction is also correctly imported at its stated
quantifiers. Its arbitrary-phase-rematching clause can in fact be
strengthened from odd \(m\ge5\) to every \(m\ge5\).

The final audited version includes the two required scope repairs:
the standing hypothesis \(m\ge2\), and a Theorem C headline separating
the fixed-offset result from the arbitrary-rematching result for odd
\(m\ge5\). Thus no exact correction remains.

The text still does not exclude arbitrary phase rematching at even
\(m=4\), and no such claim is now made.

## 1. State and footprint audit

For \(C=BA\), the displayed state formula gives the pullback coordinate
permutation

\[
c=(1,3,\ldots,2m-1)(2,4,\ldots,2m,2m+1).
\]

Thus the two coordinate cycles have lengths \(m,m+1\). Since state
labels are distinct, every state orbit has exact length \(L=m(m+1)\).
For

\[
P=[m],\qquad Q=\{2,\ldots,m+1\},
\]

one has

\[
\kappa(C^t\pi)=x_{c^tP},\qquad
\kappa(AC^t\pi)=x_{c^tQ}.
\]

This confirms the composition order: the successor footprint is \(Q\)
before applying the pullback \(c^t\), not \(c^{-t}Q\).

For \(m\ge2\), each intersection of \(P\) or \(Q\) with either coordinate
cycle is a nonempty proper cyclic interval. Hence its only simultaneous
phase stabilizer is zero modulo both \(m\) and \(m+1\), and each owner
shore has support exactly \(L\). Also \(A\mathcal O\cap\mathcal O\) is
empty: equality \(A\pi=C^t\pi\) would force equality of coordinate
permutations, while \(C^t\) preserves each of the two coordinate cycles
and \(A\) does not.

At \(m=1\), \(P\) contains the whole one-point first cycle and misses the
second, so this paragraph of the synthesis needs the standing hypothesis
\(m\ge2\).

## 2. Even-\(m\) parity

Let \(m=2r\). On the first coordinate cycle, \(Q\cap C_0\) is the
one-step translate of \(P\cap C_0\); on the second, the two intersections
are equal. The phase is therefore determined by

\[
s\equiv1\pmod m,\qquad s\equiv0\pmod{m+1},
\]

whose exact solution modulo \(L\) is \(s=m+1\). Thus

\[
c^{m+1}P=Q
\]

and

\[
\kappa(AC^t\pi)=\kappa(C^{t+m+1}\pi).
\]

Consequently the source and successor owner multisets coincide on every
full orbit. Any union of full orbits has owner vector \(2d\), with
\(d\) a nonnegative integral vector. Distinct orbits cannot cancel this
identity because owner incidences carry no negative sign.

It follows exactly that capacity one forces the empty activation, and

\[
\sum_X|2d_X-1|\ge W.
\]

This applies to the strict alternating chronology. It does not apply to
general rotor circulations whose \(B\)-run lengths vary.

## 3. Odd-\(m\) depth-one audit

Let \(m=2r+1\ge3\). At middle rank, the two shore footprints have
intersection vectors

\[
(r+1,r),\qquad(r,r+1),
\]

so their owner orbits are disjoint. Since each shore has support \(L\),
one alternating component has exactly \(2L\) distinct middle owners.

At lower depth \(q=1\), the target rank is \(s=m-1=2r\), and the two
footprints are

\[
P_s=\{1,\ldots,2r\},\qquad
Q_s=\{2,\ldots,2r+1\}.
\]

Both have intersection vector \((r,r)\). On \(C_0\), \(Q_s\) is the
one-step translate of \(P_s\); on \(C_1\), it is unchanged. The same
CRT system therefore gives the exact identity

\[
Q_s=c^{m+1}P_s.
\]

Each footprint orbit has support \(L\), because both cyclic intervals
are nonempty and proper. Hence the \(2L\) depth-one occurrences have
load exactly two on \(L\) targets. This verifies both the indexing
\(s=m-1\) and the support factor \(1/2\).

For an owner-capacity-one union containing \(q\) components, their
middle-owner blocks are disjoint and \(G=2qL\). Cross-component overlap
can only decrease lower support, so support is at most \(qL=G/2\).
Since

\[
\binom{2m+1}{m-1}=\frac{m}{m+2}W,
\]

the synthesis's displayed bound follows. It remains valid for a near
owner cover \(G=W-o(W)\), where it gives
\((1/2-o(1))W\) lower holes. If \(2L\nmid W\), the exact-cover statement
is conditional but the near-cover bound is not weakened.

## 4. Packet obstruction and its exact scope

Every canonical nested-star atom has a common ordered source suffix on

\[
J=\{m+2,\ldots,2m\}.
\]

For \(m\ge3\), \(J\) meets both coordinate cycles. Therefore

\[
\bigcup_{t\in\mathbb Z_L}c^tJ=[n].
\]

If three fixed-offset phase trajectories formed an atom at every phase,
their ordered restrictions to \(J\) would agree at every phase. The
last union then forces equality at every coordinate, so the three states
and their orbits coincide. This verifies the fixed-offset clause for all
\(m\ge3\).

For arbitrary phase rematching, partitioning three full orbits into
atoms forces equality of their ordered suffix decks. When \(m=2r+1\),
the two projections of this deck are directed length-\(r\) window decks.
For \(m\ge5\), \(r\ge2\), and each deck reconstructs its directed cyclic
label order. Independent rotations of the two coordinate cycles are one
power of \(C\) by CRT, so equal decks imply equal \(C\)-orbits. This is
the imported odd-\(m\) proof.

The same proof works for even \(m=2r\ge6\): the intersections
\(J\cap C_0,J\cap C_1\) are directed intervals of lengths \(r-1\) and
\(r\), respectively. Both lengths are at least two, so both cyclic
orders are again reconstructed. Thus the stronger exact statement is:

\[
\boxed{\text{arbitrary three-orbit phase rematching is impossible for
every }m\ge5.}
\]

At \(m=4\), one projected window has length one, so the deck argument
does not determine that coordinate cycle's order. The synthesis does
not prove arbitrary-rematching impossibility there. This finite case is
irrelevant to the asymptotic no-go but should not be absorbed into an
unqualified headline.

## 5. Scope of the annulus conclusion

The conclusion closes every rotor circulation with strict chronology

\[
e\longmapsto Ae\longmapsto BAe.
\]

For even \(m\), such a circulation cannot meet owner capacity at all.
For odd \(m\), any near owner cover by its full alternating components
has linear lower depth-one defect. The canonical atom partition and its
three-orbit packet problem are therefore not needed for the odd
first-annulus obstruction; they are an additional obstruction to an
explicit all-depth cancellation realization.

No statement here rules out:

* nonalternating or variable-length \(B\)-runs;
* a chronology whose flow closure is not \(S=BA(S)\);
* general owner-transversal de Bruijn circulations;
* the constant-one conjecture itself.
