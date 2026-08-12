# Truncated-rotor chunks with a reserve-top absorber

Date: 2026-07-25

Pure mathematics only. Put

\[
n=2m,\qquad W=\binom{2m}{m},\qquad
M=m+H,\qquad N_H=\binom{2m}{m-H},
\tag{0.1}
\]

where \(H\) is the first crossing height. Thus

\[
H\sim\sqrt{m\log m},\qquad
MN_H=W-o(W),\qquad HN_H=o(W).
\tag{0.2}
\]

The truncated radius satisfies \(Q=o(H)\). Ranks deeper than \(Q\) are
handled by the already audited packet reservoir and tails at total cost
\(o(W)\).

## 0. Verdict

The two-stage reserve construction does adapt to truncated carrier-rotor
chunks. The truncation improves one localized absorber cell from cost
\(O(H)\) to cost \(O(Q)\). The resulting signed-repair scale is

\[
\boxed{S=o(W/Q),}
\tag{0.3}
\]

not merely \(S=o(W/H)\).

There is also an exact obstruction. A short-chunk owner near-factor
controls only the middle row. An \(o(W)\)-cost rotor reserve can finish it
only if every protected row already has \(o(W)\) holes and those rowwise
leaves admit a common integral cover by legal flag columns. A linear leave
in even one protected row costs \(\Omega(W)\) to repair in this
architecture.

The weakest honest residual metric is therefore not aggregate holes,
Johnson transport, or pair discrepancy. It is the integral
**rotor reserve-cover cost**: the minimum literal length of hosted
radius-\(Q\) chunks and individual patches covering the entire remaining
flag tuple. The other metrics have the following roles.

* Aggregate holes \(o(W)\) are a crude sufficient condition, by individual
  literal repair, but are stronger than necessary.
* Rowwise holes \(o(W)\) are necessary but not sufficient.
* Johnson transport and pair discrepancy are necessary diagnostics only
  when one prescribes a signed load correction.
* Capacitated Hall on a sparse reserve-top family is an exact hosting
  condition for a proposed integral octahedral decomposition.

A concrete two-stage certificate with \(R\) reserve tops, \(S\) localized
cells, and \(E\) final literal exceptions has added cost

\[
\boxed{
\Phi_Q
=E+(M+2Q+1)R+(12Q+8)S.
}
\tag{0.4}
\]

Thus

\[
E=o(W),\qquad R=o(N_H),\qquad S=o(W/Q),
\tag{0.5}
\]

together with exact final coverage and sparse host Hall, proves
coefficient one.

## 1. Short primary chunks and their reset threshold

Fix a carrier \(U\in\binom{[2m]}M\). A radius-\(Q\) quotient state is

\[
\omega=(L;z_1,\ldots,z_{2Q};R_U),
\tag{1.1}
\]

where

\[
|L|=m-Q,\qquad |R_U|=H-Q,
\tag{1.2}
\]

and the displayed parts partition \(U\). It exposes

\[
L_q(\omega)=L+z_1+\cdots+z_{Q-q},
\qquad
U_q(\omega)=L+z_1+\cdots+z_{Q+q}
\tag{1.3}
\]

for \(0\le q\le Q\), with middle owner

\[
X(\omega)=L+z_1+\cdots+z_Q.
\tag{1.4}
\]

Let a primary family \(\mathscr P\) consist of \(p\) directed rotor
chunks, with \(s_i\) state endpoints in chunk \(i\), and put

\[
T=\sum_{i=1}^p s_i.
\tag{1.5}
\]

The first state of a chunk costs \(2Q+2\) letters and every later state
costs one. Hence the primary length is exactly

\[
\boxed{
|w(\mathscr P)|
=\sum_i(s_i+2Q+1)
=T+(2Q+1)p.
}
\tag{1.6}
\]

In the intended regime \(T=(1-o(1))W\), coefficient one requires

\[
Qp=o(W).
\tag{1.7}
\]

If the average chunk length is \(\ell=T/p\), this is

\[
\boxed{\ell=\omega(Q).}
\tag{1.8}
\]

Thus chunks may satisfy \(Q\ll\ell\ll M\). Chunks of length \(O(Q)\) are
fatal by reset cost alone.

### Path-hitting form

At an interior start of an owner path,

\[
L_q(t)=\bigcap_{i=0}^{q}X_{t+i},
\qquad
U_q(t)=\bigcup_{i=0}^{q}X_{t-i}.
\tag{1.9}
\]

Consequently a lower target
\(A\in\binom{[2m]}{m-q}\) is hit precisely when a consecutive
\((q+1)\)-vertex owner path lies in

\[
\mathcal U_A
=\left\{
X\in\binom{[2m]}m:A\subset X
\right\}.
\tag{1.10}
\]

This is the relevant up-set path-hitting formulation. Upper flags are
given by the union formula, equivalently by complementary lower data with
the corresponding shifted depth. No reduction to singleton
near-universal cycles is used.

The first and last \(q\) positions of a finite chunk are boundary collars
for (1.9); their actual flags remain exactly those in (1.3). If one
discards collar information, the loss is at most \(2qp\) occurrences at
signed depth \(q\), and at most \(O(Q^2p)\) over the whole protected
window. Therefore:

* rowwise collar loss is \(o(W)\) under the necessary reset condition
  \(Qp=o(W)\);
* the stronger aggregate estimate \(Q^2p=o(W)\) would require average
  chunk length \(\omega(Q^2)\);
* a simultaneous column cover can avoid imposing the latter scale.

## 2. Exact hole identities

Let

\[
\mathcal K_Q=\{m-Q,\ldots,m+Q\},
\tag{2.1}
\]

counting the middle rank only once. For \(k\in\mathcal K_Q\), define

\[
\mu_k(A)
=\#\{\text{primary endpoints exposing }A\},
\tag{2.2}
\]

\[
\mathcal H_k
=\left\{
A\in\binom{[2m]}k:\mu_k(A)=0
\right\},
\qquad
h_k=|\mathcal H_k|.
\tag{2.3}
\]

Every endpoint contributes one occurrence at every protected rank, so
the total load at rank \(k\) is \(T\). Put

\[
\mathcal E_k
=\sum_{A\in\binom{[2m]}k}(\mu_k(A)-1)_+.
\tag{2.4}
\]

Then

\[
\boxed{
h_k=\binom{2m}{k}-T+\mathcal E_k.
}
\tag{2.5}
\]

This is an identity. At \(k=m\) it is the owner ledger. Thus an owner
near-factor controls \(\mathcal E_m\), but does not control
\(\mathcal E_k\) for \(k\ne m\). At depth one, for example, flag
coverage asks which intersections of directed Johnson edges occur; the
owner set alone contains no such edge-factor information.

## 3. The exact integral reserve metric

### Definition 3.1 (rotor reserve-cover cost)

For the hole tuple

\[
\mathcal H=(\mathcal H_k:k\in\mathcal K_Q),
\tag{3.1}
\]

define \(\operatorname{RCov}_Q(\mathcal H)\) to be the minimum of

\[
\sum_{C\in\mathscr C}|C|
+(2Q+1)|\mathscr C|
+E
\tag{3.2}
\]

over the following integral data.

1. \(\mathscr C\) is a family of legal directed radius-\(Q\) rotor
   chunks, each hosted in an allowed reserve top.
2. There are \(E\) individual literal target patches.
3. Every \(A\in\mathcal H_k\) is either exposed as the rank-\(k\) flag
   of an endpoint in \(\mathscr C\), or is one of the \(E\) literal
   patches.

Repeated states and repeated targets are fully charged. There is no
fractional credit. Host restrictions and reset counts are part of the
minimum.

### Theorem 3.2 (exact reserve completion)

If

\[
T+(2Q+1)p\le W+o(W)
\tag{3.3}
\]

and

\[
\operatorname{RCov}_Q(\mathcal H)=o(W),
\tag{3.4}
\]

then the standard construction for \(q>Q\), together with the primary
and reserve chunks, has length \(W+o(W)\) and covers all required
targets.

#### Proof

Compile the primary by (1.6). Compile an integral minimizer in
Definition 3.1 and append its literal patches. Every protected hole is
then covered. Concatenation preserves witnesses internal to earlier
chunks. The audited outer packet reservoir and tails cost \(o(W)\).
Equations (3.3) and (3.4) give the length bound. \(\square\)

This theorem is deliberately exact: \(\operatorname{RCov}_Q\) is the
actual additional literal cost inside the truncated-rotor compiler.

### Necessary scalar bounds

Let

\[
h_\Sigma=\sum_{k\in\mathcal K_Q}h_k.
\tag{3.5}
\]

One reserve endpoint exposes only one target in a fixed row and at most
\(2Q+1\) protected targets in total. An individual patch covers only one
target. Therefore

\[
\boxed{
\operatorname{RCov}_Q(\mathcal H)
\ge\max_{k\in\mathcal K_Q}h_k,
\qquad
\operatorname{RCov}_Q(\mathcal H)
\ge\frac{h_\Sigma}{2Q+1}.
}
\tag{3.6}
\]

It follows that any \(o(W)\) reserve completion must satisfy

\[
\max_k h_k=o(W),
\qquad
h_\Sigma=o(WQ).
\tag{3.7}
\]

These conditions are not sufficient: they do not encode nesting,
carrier containment, rotor connectivity, or reset count.

The old aggregate condition

\[
h_\Sigma=o(W)
\tag{3.8}
\]

is sufficient by individual literal repair. It is stronger than
necessary. If all holes lie in \(t=o(W)\) legal flag columns, grouped into
\(c\) chunks with \(Qc=o(W)\), then the reserve costs \(o(W)\) even when
\(h_\Sigma\) is as large as \((2Q+1)t\).

## 4. Rotorizing one localized absorber cell

Fix a reserve top \(U\), a cyclic order \(C\) on \(U\), and two disjoint
adjacent swaps. For one swap boundary \(b\), all possibly affected phase
starts throughout the protected window lie in

\[
B_Q(b)
=\{b-m+1\}
\cup
\{b-Q+1,\ldots,b+Q+1\}.
\tag{4.1}
\]

Thus

\[
|B_Q(b)|\le 2Q+2,
\tag{4.2}
\]

and \(B_Q(b)\) is a union of at most two cyclic intervals. Each positive
diagonal configuration uses two orders restricted to \(B_Q(b)\).
Therefore it contains at most

\[
4Q+4
\tag{4.3}
\]

state endpoints and is a union of at most four promotion segments.

Every promotion segment is a legal truncated-rotor trajectory. A segment
with \(s\) states costs \(s+2Q+1\), not \(s+2H\). Hence one positive
diagonal costs at most

\[
\boxed{
c_Q
=(4Q+4)+4(2Q+1)
=12Q+8.
}
\tag{4.4}
\]

This is the basic gain from truncation.

Define the safe per-top bank size

\[
L_Q
=\left\lfloor
\frac{M}{2(12Q+8)}
\right\rfloor.
\tag{4.5}
\]

Then one reserve top hosts \(L_Q\) separately compiled cells at total
cell cost at most \(M/2\), and

\[
L_Q=\Theta(M/Q).
\tag{4.6}
\]

The added middle occurrences are at most
\((4Q+4)L_Q<M/4\).

## 5. The explicit two-stage theorem

Starting from the primary chunks, choose:

* \(R\) reserve tops;
* one base length-\(M\), radius-\(Q\) rotor trajectory on each reserve
  top;
* \(S\) localized cells, at most \(L_Q\) on each reserve top, with one
  positive diagonal selected integrally in every cell;
* \(E\) targets still uncovered after all final diagonal choices.

Patch the last \(E\) targets literally.

### Theorem 5.1 (two-stage truncated-rotor reserve)

The additional protected-band word length is at most

\[
\boxed{
\Phi_Q
=E+(M+2Q+1)R+(12Q+8)S.
}
\tag{5.1}
\]

If \(\Phi_Q=o(W)\), the outer reservoir and tails complete a
\(W+o(W)\) construction.

#### Proof

Each base trajectory costs \(M+2Q+1\). Equation (4.4) charges every
state and every reset of each localized cell. The remaining \(E\) patches
cost \(E\). All selected configurations are positive, literal, and
integral. By the definition of \(E\), every protected target is covered
after the final choices. The outer construction costs \(o(W)\).
\(\square\)

A convenient sufficient scale is

\[
\boxed{
E=o(W),\qquad
R=o(N_H),\qquad
S=o(W/Q).
}
\tag{5.2}
\]

Indeed \(MN_H=W-o(W)\) and \(QN_H=o(W)\), so the reserve-base term is
\(o(W)\); the cell term is \(o(W)\).

Compactly packing \(S\) cells at capacity (4.5) would use

\[
R=O(SQ/M).
\tag{5.3}
\]

Thus \(S=o(W/Q)\) implies \(R=o(W/M)=o(N_H)\), provided the supports
admit such compact hosting.

### Owner ledger for omitted reserve tops

Suppose the primary on nonreserve tops covers at least

\[
M(N_H-R)-E_{\rm own}
\tag{5.4}
\]

distinct middle owners. Arbitrary base trajectories on the reserve tops
then leave at most

\[
\boxed{
(W-MN_H)+MR+E_{\rm own}
}
\tag{5.5}
\]

middle holes. This bound gives no credit to reserve-owner compatibility;
it simply preserves the primary owner support. Hence

\[
R=o(N_H),\qquad E_{\rm own}=o(W)
\tag{5.6}
\]

suffice for the middle row. Localized cells are positive and cannot
destroy a base witness.

## 6. Exact obstruction to an owner-only theorem

Let \(h_k^{\rm prim}\) be the holes before the reserve stage. A reserve
base trajectory contributes at most \(M\) targets at one fixed rank. A
localized cell contributes at most \(4Q+4\) targets at one fixed rank.
The \(E\) literal patches contribute at most \(E\). Thus every certificate
in Theorem 5.1 satisfies

\[
\boxed{
h_k^{\rm prim}
\le MR+(4Q+4)S+E
\qquad(k\in\mathcal K_Q).
}
\tag{6.1}
\]

Under (5.2), the right side is \(o(W)\).

### Corollary 6.1 (one-row obstruction)

Within the truncated-rotor reserve architecture, if

\[
h_k^{\rm prim}=\Omega(W)
\tag{6.2}
\]

at one protected rank, no reserve of literal cost \(o(W)\) can finish the
primary family.

#### Proof

Every rotor endpoint supplies one flag in the fixed row, and its literal
compilation costs at least one letter. Every individual patch also costs
one letter. Filling \(h_k^{\rm prim}\) distinct holes therefore costs at
least \(h_k^{\rm prim}\). \(\square\)

This is the sharp immediate obstruction to starting only with a
short-chunk owner near-factor. The owner condition gives \(h_m=o(W)\).
It contains no assertion that

\[
h_{m-q}^-=o(W),\qquad h_{m+q}^+=o(W)
\tag{6.3}
\]

for \(1\le q\le Q\). By (1.9), those are consecutive path-hitting
requirements, not vertex-owner requirements.

Accordingly, an owner near-factor can be completed only after one proves
one of the following genuinely stronger statements:

1. the exact reserve metric
   \(\operatorname{RCov}_Q(\mathcal H)=o(W)\);
2. an explicit hosted localized-cell certificate satisfying (5.1);
3. the older, stronger aggregate bound \(h_\Sigma=o(W)\).

The reserve theorem does not manufacture flag near-coverage from owner
near-coverage.

## 7. Signed load correction

Pure coverage uses positive reserve chunks. It has no point-margin,
pair-margin, parity, or Johnson-transport invariant. These quantities
enter only if reference diagonals are fixed and the binary cell choices
must realize a prescribed signed load correction.

Let \(z_k\) be the desired correction at protected rank \(k\). A localized
cell changes exactly one protected rank by one coefficient-one
octahedron. If \(S\) cells realize \(z=(z_k)\), then

\[
A_1z_k=0
\qquad(k\in\mathcal K_Q),
\tag{7.1}
\]

and

\[
\boxed{
S
\ge
\frac12
\sum_k W_1^J((z_k)_+,(z_k)_-),
}
\tag{7.2}
\]

\[
\boxed{
S
\ge
\frac14
\sum_k\|A_2z_k\|_1.
}
\tag{7.3}
\]

Therefore an \(o(W)\)-cost rotorized signed absorber requires

\[
\sum_k W_1^J((z_k)_+,(z_k)_-)=o(W/Q),
\tag{7.4}
\]

\[
\sum_k\|A_2z_k\|_1=o(W/Q).
\tag{7.5}
\]

These are necessary, not sufficient. Equal point margins and small
\(\ell^1\) defect do not bound the route length. Constant defect can have
Johnson cost \(\Omega(H)\), and the pair-moment examples require
\(\Omega(m^2D)\) octahedra for defect \(D\).

Even the generic full-reservoir upper bound

\[
S=O(m^2D)
\tag{7.6}
\]

would be compatible with rotorized cost \(o(W)\) only at

\[
D=o\left(\frac{W}{m^2Q}\right),
\tag{7.7}
\]

and still needs positive donors and legal hosts. This is far stronger
than a generic \(o(W)\) hole estimate.

## 8. Exact sparse host Hall

A rank-\(k\) octahedron has coordinate support \(F\) of size \(k+2\).
It can be installed in a top \(U\) exactly when

\[
F\subseteq U.
\tag{8.1}
\]

Let \(\mathcal D\) be the multiset of proposed cells and
\(\mathcal R\) a chosen family of reserve tops. Join a cell to each
containing top in \(\mathcal R\). There is an assignment using at most
\(L_Q\) cells per top if and only if

\[
\boxed{
|\mathcal A|
\le
L_Q|N_{\mathcal R}(\mathcal A)|
\quad
\text{for every submultiset }
\mathcal A\subseteq\mathcal D.
}
\tag{8.2}
\]

This is capacitated Hall. It is necessary and sufficient for the proposed
integral move multiset.

For coefficient one, it must hold on a sparse witness family

\[
|\mathcal R|=o(N_H).
\tag{8.3}
\]

Hall against all \(N_H\) tops does not imply (8.3): the move supports may
force the assignment to spread across too many tops.

Thus a signed certificate needs all of:

1. an integral octahedral decomposition of length \(S=o(W/Q)\);
2. positive final diagonal choices, with every lost reference witness
   included in the final exception set \(E\);
3. a reserve family of size \(o(N_H)\) satisfying (8.2).

Johnson and pair discrepancy audit the first item from below. They replace
neither integrality nor sparse hosting.

## 9. Weakest usable TRP residual scales

The hierarchy is now explicit.

### Exact integral gate

\[
\boxed{
T+(2Q+1)p\le W+o(W),
\qquad
\operatorname{RCov}_Q(\mathcal H(\mathscr P))=o(W).
}
\tag{9.1}
\]

This is the weakest gate proved by the literal truncated-rotor compiler.
It includes holes, vertical nesting, host containment, chunk connectivity,
and resets in the quantity actually paid.

### Localized-absorber gate

It is enough to exhibit an integral certificate with

\[
\boxed{
E+(M+2Q+1)R+(12Q+8)S=o(W),
}
\tag{9.2}
\]

exact final flag coverage, and sparse host Hall. If a prescribed signed
correction is used, add the lattice and positivity conditions in
Sections 7 and 8.

### Crude hole gate

\[
\sum_{k\in\mathcal K_Q}h_k=o(W)
\tag{9.3}
\]

remains sufficient by literal repair, taking \(R=S=0\). It discards all
vertical sharing.

### Necessary scalar tests

\[
\max_k h_k=o(W),
\qquad
\sum_k h_k=o(WQ).
\tag{9.4}
\]

For signed correction, (7.4), (7.5), and sparse host Hall are also
necessary. None of these scalar tests is sufficient.

## 10. Final coefficient-one ledger

For a short-chunk primary with \(T\) endpoints and \(p\) chunks, and a
two-stage reserve with parameters \(R,S,E\), the complete even-dimensional
word has length

\[
\begin{aligned}
L
&\le T+(2Q+1)p\\
&\quad +(M+2Q+1)R+(12Q+8)S+E\\
&\quad +o(W),
\end{aligned}
\tag{10.1}
\]

where the last term is the corrected \(q>Q\) reservoir and the two tails.
Every displayed summand is literal and integral.

A proved coefficient-one route is therefore

\[
T=W-o(W),\qquad Qp=o(W),
\tag{10.2}
\]

\[
E=o(W),\qquad R=o(N_H),\qquad S=o(W/Q),
\tag{10.3}
\]

plus actual final protected-flag coverage and sparse capacitated hosting.

What remains open is not the reserve ledger. It is the construction of
the required integral protected-band certificate from a short-chunk owner
near-factor. The exact immediate obstruction is a linear leave in one
protected row. Below that threshold, the live problem is a joint
path-transversal: assemble the rowwise leaves into \(o(W)\)-cost legal flag
columns, or into \(o(W/Q)\) hosted localized cells plus \(o(W)\) literal
exceptions.
