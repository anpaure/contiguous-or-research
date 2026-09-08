# A highest-valley four-packet theorem for native MSW common-history connectivity

**Date:** 2026-08-13  
**Status:** unconditional all-parameter symbolic theorem.  The context,
packet, residue-order, wrap-gap, and exceptional-cut calculations were
independently hostile-audited on 2026-08-14; see
MATH_AUDIT_MSW_HIGHEST_VALLEY_FOUR_PACKET_RESIDUE_AND_CONTEXT_20260814.md.

## 0. Statement

For integers \(d\ge1\), put

\[
n=2m+1,\qquad R=m+1,\qquad s=R-d.
\]

For a canonical tight MSW order \(w=(w_i)_{i\in\mathbb Z_n}\), a cut
\(a\) has forced endpoint rail

\[
F_j(w,a)=\{w_{a+j},w_{a+s-1+j}\},\qquad 0\le j<d.
\]

Two Dyck roots are same-forced adjacent if they differ by one zero-one
transposition and, after cuts and orientations,

\[
F_j(w,a)=F_j(w',b)\qquad(0\le j<d).
\]

### Theorem 0.1

If

\[
m\ge 3d+1,
\]

then every nonmountain Dyck root has a same-forced neighbour of strictly
larger area.  The neighbour is obtained at a highest valley by one of

\[
01\to10,\qquad
001\to100,\qquad
011\to110,\qquad
0011\to1010.
\]

Consequently the native same-forced graph is connected and contains a
monotone arborescence to the mountain \(1^m0^m\).

This closes connectivity only.  A common-history source fusion still
requires a simultaneous coalesced separated-port assignment on the chosen
tree; identical incidence histories may reuse one port as in
`MATH_THEOREM_COALESCED_MULTIINCIDENCE_COMMON_HISTORY_EULER_FUSION_20260814.md`.

## 1. Highest-valley normal form

Choose a valley \(01\) of maximum height.  The excursion immediately
closed on its left and the excursion immediately opened on its right are
pyramids: otherwise one of them contains a strictly higher valley.  Write
\(L\) and \(Q\) for their interior semilengths and \(O\) for the remaining
exterior semilength.  Then

\[
L+Q+O=m-2.
\]

Up to a Dyck context the marked factor is

\[
1^{L+1}0^{L+1}\,1^{Q+1}0^{Q+1}.
\]

The four moves in Theorem 0.1 are exactly the possible enlargements of the
central valley by its adjacent bits.  Each moves a zero rightward across a
one, remains Dyck, and strictly increases area.

## 2. Context transport

The MSW flip word obeys

\[
\rho(1u0v)=\bigl(c,c-\rho(\mu u),1,c+\rho(v)\bigr),
\qquad c=|u|+2,
\]

and

\[
\rho(\mu u)=|u|+1-\operatorname{rev}\rho(u).
\]

Mark the smallest Dyck factor containing the two adjacent pyramids and
move from it to the root along its binary-tree address.  At a right
address step the active old-to-new position permutation is translated and
an identical fixed block is appended.  At a left step it is translated
and reversed, and again an identical fixed block is appended.  Induction
therefore proves:

### Lemma 2.1

For a highest-valley packet, the global old-to-new flip-position
permutation is dihedrally conjugate to the canonical local permutation
with \(2O\) additional fixed positions inserted in its one cyclic exterior
gap.  Including the always-fixed sentinel, the exterior fixed interval has
length \(2O+1\).
Thus common-rail existence depends only on \(L,Q,O\).  The shape of the
ambient context changes label order inside the fixed block but not the
position calculation; an odd number of left address steps reverses it.

#### Proof

Suppose first that the marked child is the right child \(v\) in
\(1u0v\), and put \(e=|u|/2+1\).  The two copies of \(u\) are identical.
The recursion therefore places the old-to-new permutation of \(v\),
translated, in one contiguous block and fixes the other \(2e\) flip
positions pointwise.

If the marked child is the left child \(u\), put \(e=|v|/2+1\).  The
identity

\[
\rho(\mu u)=|u|+1-\operatorname{rev}\rho(u)
\]

conjugates the child permutation by reversal and translation.  All
positions contributed by \(v\) and the enclosing pair are fixed.  They
occur at the two linear ends of the displayed recursion, hence form one
interval on the cyclic flip-position circle, again of total length
\(2e\).

For the induction, cut the child's cyclic position circle immediately
before its active recursion block.  Maintain the stronger invariant that
all exterior fixed positions occupy the complementary cyclic interval at
the two linear ends.  A right step puts its new fixed prefix at one end.
A left step reverses the active block and puts its fixed prefix and suffix
at the two ends.  Thus the new fixed positions extend, and never split,
the existing exterior interval; reversal merely exchanges its ends.

Summing \(e\) along the address gives the exterior semilength \(O\), so
induction inserts exactly \(2O\) additional fixed positions beside the
sentinel in one cyclic gap.  The only possible change to the active
permutation is the accumulated dihedral conjugacy.  Such a conjugacy
translates or reverses every cut and preserves common-rail existence.
\(\square\)

## 3. Explicit packet permutations

Use the canonical representative

\[
X=M_{L+1}M_{Q+1}M_O,\qquad M_t=1^t0^t,
\]

and put \(A=2L+2\), \(B=2Q+2\).  Index the old flip word by
\(0,1,\ldots,n-1\).  If \(\pi\) records, at each new position, the old
position occupying it, the flip recursion gives

\[
\begin{array}{c|l}
01&(A,\ldots,A+B-2,0,A+B-1,1,\ldots,A-1)\\
001&(A,\ldots,A+B-2,1,\ldots,A-3,0,A-2,A+B-1,A-1)\\
011&(A,0,A+1,A+B-1,A+2,\ldots,A+B-2,1,\ldots,A-1)\\
0011&(A,1,\ldots,A-3,0,A-2,A+1,A+B-1,
       A+2,\ldots,A+B-2,A-1).
\end{array}
\]

After the displayed prefix, \(\pi\) is the identity.  Empty ranges are
omitted.  Hence in the four cases needed later,

\[
\begin{array}{c|c}
01,\ A=B=2&\{0,1,2,3\}\\
001,\ B=2&\{0,A-2,A-1,A,A+1\}\\
011,\ A=2&\{0,1,2,3,A+B-1\}\\
0011&\{0,A-2,A-1,A,A+1,A+B-1\}
\end{array}
\]

are the nonfixed flip positions.

Let

\[
\iota(z)=2^{-1}z\pmod n,\qquad 2^{-1}=m+1\pmod n,
\]

and let \(C_\pi=\iota(\operatorname{supp}(\pi-\mathrm{id}))\).  A
same-start direct cut \(a\) exists whenever the cyclic interval
\([a,a+d-1]\) avoids

\[
\mathcal B_\pi=C_\pi\cup(C_\pi-(s-1)).
\]

Indeed, the first copy protects the first endpoint rail and the translate
protects the second.  Such a cut exists exactly when two consecutive
points of \(\mathcal B_\pi\) have cyclic distance at least \(d+1\).

## 4. The four residue cases

### Lemma 4.1

At a highest valley, one of the following sufficient alternatives holds.

\[
\begin{array}{c|c|c}
\text{local case}&\text{sufficient inequality}&\text{packet}\\ \hline
L=Q=0&O\ge2d&01\\
L>0,\ Q=0&L+O\ge2d&001\\
L=0,\ Q>0&Q+O\ge2d&011\\
L,Q>0&L+Q+O\ge3d-1&0011.
\end{array}
\]

In the last row the direct \(0011\) rail has one exception,

\[
(L,Q,O)=(d,d,d-1).
\]

At that exception both \(001\) and \(011\) have crossed common rails.

#### Proof

For \(L=Q=0\), the first half of \(\mathcal B_\pi\) is

\[
\{0,1,O+3,O+4\}.
\]

After its translate by \(-(O+2-d)\) is inserted, the gap from \(d+2\) to
\(O+3\) has length \(O-d+1\), at least \(d+1\) when \(O\ge2d\).

For \(L>0,Q=0\), the first half is

\[
\{0,L,L+1,2L+O+3,2L+O+4\}.
\]

Put \(T=L+O\).  If \(O\le d-2\), the translated point
\(d-O-1\) is immediately before \(L\), leaving gap

\[
L-(d-O-1)=T-d+1\ge d+1.
\]

If \(O\ge d-1\) and \(L\ge d+1\), the gap \(0\) to \(L\) works.  Finally,
if \(O\ge d-1\) and \(L\le d\), then \(T\ge2d\) implies \(O\ge d\);
the translated point \(L+d+2\) and the next old point \(T+L+3\)
leave gap

\[
 (T+L+3)-(L+d+2)=T-d+1\ge d+1.
\]

This proves the \(001\) row.  Reversal proves the \(011\) row.

Suppose now \(L,Q>0\), and put \(T=L+Q+O\).  For \(0011\), the first half
of \(\mathcal B_\pi\), in tight-position cyclic order, is

\[
0,\ L,\ L+1,\ T+L+3,\ T+L+4,\ T+L+Q+4.
\]

Assume \(T\ge3d-1\), but no gap in \(\mathcal B_\pi\) has length \(d+1\).
If \(Q+O\le d-2\), the translated point \(d-Q-O-1\) is immediately before
\(L\), and the resulting gap is

\[
L-(d-Q-O-1)=T-d+1\ge2d,
\]

a contradiction.  Therefore \(Q+O\ge d-1\), so the translated pair from
\(L,L+1\) lies in the final segment before the cyclic wrap.  Thus \(0,L\) are
consecutive, and the no-gap assumption gives \(L\le d\).  By reversal,
\(Q\le d\).  Hence \(O\ge d-1\).

In this cyclic order, the translated point from \(T+L+Q+4\) is
\(L+Q+d+2\).  Its next old point is \(T+L+3\), so one gap has length

\[
L+O+1-d.
\]

The last translated point is \(T+L+d+4\); its wrap to zero has length

\[
Q+O+1-d.
\]

Both are at most \(d\).  Therefore

\[
L+O\le2d-1,\qquad Q+O\le2d-1.
\]

Adding gives \(L+Q+2O\le4d-2\), or \(T+O\le4d-2\).
Using \(T\ge3d-1\) yields \(O\le d-1\).  Since already
\(O\ge d-1\), equality holds.  Then \(L,Q\le d\) and
\(L+Q+O\ge3d-1\) force \(L=Q=d\).  Thus the displayed triple is the only
direct \(0011\) exception.

At that triple \(m=3d+1\), \(n=6d+3\), and \(s=2d+2\).  Substitution in
the explicit packet permutations gives crossed rails for \(001\) at cuts

\[
(a,b)=(d+1,4d+2),
\]

and for \(011\) at cuts

\[
(a,b)=(d+2,4d+4).
\]

More explicitly, if \(q_r\) is the old tight position occupying new tight
position \(r\), then the \(001\) permutation gives

\[
 q_j=d+1+j,\qquad q_{4d+2+j}=3d+2+j,
\]

while the \(011\) permutation gives

\[
 q_{2+j}=d+2+j,\qquad q_{4d+4+j}=3d+3+j
\]

for every \(0\le j<d\), with indices modulo \(n\).  Since \(s-1=2d+1\),
these are exactly the two crossed ordered endpoint identities at the
displayed cuts.
Context transport only translates or reverses these cuts.  This proves
the lemma.  \(\square\)

## 5. Proof of Theorem 0.1

At a highest valley,

\[
L+Q+O=m-2\ge3d-1.
\]

If both adjacent pyramids are nontrivial, the last row of Lemma 4.1
applies.  If exactly one is trivial, the corresponding middle sum equals
\(m-2\ge2d\).  If both are trivial, \(O=m-2\ge2d\).  Hence one of the four
packets is same-forced and area-increasing.

Iteration terminates because area strictly increases.  A Dyck word with
no valley is the mountain, proving monotone connectivity.  \(\square\)

## 6. Exact H100 replay

The targeted verifier is
\(scratch/audit_same_forced_packet_only.cpp\); the full graph verifier is
\(scratch/audit_msw_common_history_graph.cpp\).  All runs were executed on
H100.

\[
\begin{array}{c|c|c|c}
m&d&|D_m|&\text{four-packet failures}\\ \hline
10&3&16{,}796&0\\
13&4&742{,}900&0\\
14&4&2{,}674{,}440&0.
\end{array}
\]

For \(m=13,d=4\), the full same-forced graph has

\[
15{,}530{,}841
\]

edges, minimum degree \(16\), maximum degree \(138\), and one component.
The greedy monotone replay has no orphan and maximum child load \(3\).

Frozen artifact digests:

\[
\begin{array}{c|c}
\text{artifact}&\text{SHA256}\\ \hline
\text{full verifier}&
0f6513192b56341b1e6b679ab2016a22513f02d9e427c327ed6a389a87da80b0\\
\text{\(m=13\) full output}&
79832361c73a21b32e1c9696475768144f4765e7f7dd6e53f24e5d0ccc2076b3\\
\text{targeted verifier}&
50e5886ce85deefd6da024c7d3803617ac8dc84a40e254c12bb094fb26d25378\\
\text{\(m=14\) targeted output}&
362ea6ed8ee066e0b4cb4dd0c06efe66566ed1bb609591dd97f3663f41af3916.
\end{array}
\]

## 7. Remaining all-parameter common-history gate

Connectivity does not imply simultaneous source realization.  The
multi-block theorem permits length-\(d\) ports with cyclic start gaps at
least \(d+1\), and one tight row has raw separated-port capacity

\[
\left\lfloor\frac{2m+1}{d+1}\right\rfloor.
\]

Several incidences may coalesce when they request the same start and
literal history.  At the first threshold \((m,d)=(10,3)\), the exact
coalesced incidence CSP is feasible: one orientation per row, one parent
per nonmountain root, and cyclic gap at least \(d+1\) between distinct
used starts.  H100 found and independently replayed a full
\(16{,}795\)-edge arborescence.  It has child histogram

\[
\{0:5627,\ 1:6229,\ 2:4261,\ 3:672,\ 4:7\},
\]

only (28) rows use four distinct ports, and (5{,}695) rows coalesce at
least two incidences at one port.  This is finite evidence, not yet an
all-parameter port theorem.

The exact remaining native problem is to prove an all-(m) coalesced
separated-port selection for the highest-valley parent DAG (or a broader
same-forced DAG).  The long upper deck remains a later current/actuator
problem.
