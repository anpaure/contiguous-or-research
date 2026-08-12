# The SCD common-history gate begins with a residence ordering of the top targets

**Date:** 2026-08-07
**Method:** coordinatewise interval supports, delayed intersection atoms,
random-permutation exposure, and the BTK interface law
**Status:** unconditional top-row equivalence, a literal positive
construction under residence, and proof-safe no-go results for random
endpoint order and the natural BTK/GMM chronology.  The result does not
order all SCD pieces or prove the adaptive-phase merged PBBS chart theorem.

## 1. Top targets already impose a private-point condition

Use the odd merged-PBBS parameters and put

\[
r=t-1=m-d-1,\qquad
\mathcal T=\binom{[n]}r,\qquad
A=|\mathcal T|.
\tag{1.1}
\]

Every rank-\(r\) target is the maximum of one top SCD piece.  If that piece
is assigned to endpoint \(e\), its target uses the maximal suffix interval

\[
I_e=[e-d+1,e].
\tag{1.2}
\]

Let \(\mathcal E\) be the physical endpoint cycle.  For a coordinate \(x\),
call \(p\in\mathcal E\) **top-allowed** when every top target whose interval
contains \(p\) contains \(x\).  Equivalently,

\[
p\in E_x^{\rm top}
\quad\Longleftrightarrow\quad
x\in T_e
\text{ for every top endpoint }e\in[p,p+d-1].
\tag{1.3}
\]

### Proposition 1.1 (top private-point necessity)

Any common source word realizing the complete assigned SCD target family
must satisfy

\[
\boxed{
I_e\cap E_x^{\rm top}\ne\varnothing
\qquad(e\text{ top},\ x\in T_e).}
\tag{1.4}
\]

#### Proof

Let \(S_x\) be the set of source positions whose letter contains \(x\).
Since \(T_e\) contains \(x\), its interval \(I_e\) must meet \(S_x\).
Choose \(p\in I_e\cap S_x\).  Every assigned interval containing \(p\)
has a union containing \(x\); in particular every top interval containing
\(p\) has a target containing \(x\).  Thus \(p\in E_x^{\rm top}\).
\(\square\)

The actual allowed set, after all lower targets and owner envelopes are
included, is a subset of \(E_x^{\rm top}\).  Hence failure of (1.4) is an
absolute common-history obstruction.

## 2. Exact positive construction when top endpoints are consecutive

First consider a cyclic list

\[
T_0,T_1,\ldots,T_{L-1}\in\binom{[n]}r
\tag{2.1}
\]

with one top target at every endpoint.  Repetitions are allowed in this
local statement.  Define delayed intersection atoms

\[
B_p=\bigcap_{j=0}^{d-1}T_{p+j}.
\tag{2.2}
\]

All indices are cyclic.

For a coordinate \(x\), write its membership word

\[
\epsilon_i(x)=\mathbf 1_{\{x\in T_i\}}.
\]

### Theorem 2.1 (top-row residence equivalence)

The following are equivalent.

1. Every cyclic \(1\)-run of every coordinate membership word
   \(\epsilon(x)\) has length at least \(d\).
2. Every incidence \((T_e,x)\), \(x\in T_e\), satisfies the private-point
   condition (1.4).
3. The atom sequence \(B=(B_p)\), allowing an empty atom at this purely
   set-theoretic stage, realizes every top target exactly:

   \[
   \boxed{
   T_e=\bigcup_{p=e-d+1}^{e}B_p
   \qquad(e\in\mathbb Z_L).}
   \tag{2.3}
   \]

#### Proof

The interval \(I_e\) meets \(E_x^{\rm top}\) exactly when there is a
length-\(d\) cyclic window of \(1\)'s in \(\epsilon(x)\) which contains
the occurrence at \(e\).  This holds for every \(1\)-occurrence exactly
when every \(1\)-run has length at least \(d\).  Hence Items 1 and 2 are
equivalent.

For every \(p\in I_e\), the \(d\)-window defining \(B_p\) contains \(e\).
Thus \(B_p\subseteq T_e\), proving

\[
\bigcup_{p\in I_e}B_p\subseteq T_e.
\]

If \(x\in T_e\), Item 1 supplies a length-\(d\) all-\(x\) window
containing \(e\); its start \(p\) lies in \(I_e\) and \(x\in B_p\).
This proves the reverse inclusion and Item 3.

Conversely, Item 3 gives, for every \(x\in T_e\), a
\(p\in I_e\) with \(x\in B_p\).  The defining \(d\)-window of \(B_p\)
is an all-\(x\) window containing \(e\), proving Item 1. \(\square\)

The theorem is a genuine positive common-history construction for the
maximal target row whenever all atoms are nonempty.  It also identifies
the exact structure a proposed Gray order must have: coordinate residence,
not merely adjacency or target distinctness.

### Corollary 2.2 (safe Johnson ordering suffices for the top row)

Suppose consecutive \(T_i\)'s are Johnson adjacent and no coordinate is
deleted less than \(d\) steps after insertion.  Then every positive
coordinate run has length at least \(d\), so (2.2) realizes the top row.
In this case every atom has rank \(r-d+1>0\), and hence is a legal
nonempty source letter.

If deletion and insertion labels are both unrepeated in every \(d\)-edge
window, the order is two-sided resident and the same atoms also have the
usual geodesic intersection identities.

This corollary does not assert that such a Johnson Hamilton cycle exists.

## 3. Random endpoint permutation fails exponentially in \(d\)

Let the merged region have \(g\) endpoint positions, where

\[
\frac Ag\longrightarrow
\rho_0:=\frac{e^{-\pi/4}}{1-e^{-\pi/4}}>0.
\tag{3.1}
\]

Choose \(A\) top positions uniformly from the \(g\)-cycle and biject
\(\mathcal T\) uniformly to them.  All remaining pieces and targets are
ignored; this makes the private-point test only easier.

### Theorem 3.1 (random-order top-row no-go)

For the random assignment above, the expected fraction of incidences

\[
(e,x),\qquad e\text{ top},\quad x\in T_e,
\]

which satisfy (1.4) is at most

\[
\boxed{
d\left(
e^{-c_1d}+2^{\,1-c_2d}
\right)=e^{-\Omega(d)},}
\tag{3.2}
\]

for positive constants \(c_1,c_2\) depending only on \(\rho_0\).
Consequently, with probability \(1-o(1)\), all but \(o(Ar)\) top
incidences fail the necessary common-history condition.

#### Proof

Condition on a top incidence \((e,x)\) and fix
\(p\in I_e\).  Let \(K_p\) be the number of top endpoints in the
length-\(d\) window \([p,p+d-1]\).  This window contains \(e\), and the
other top positions form a hypergeometric sample with mean
\((\rho_0+o(1))d\).  The standard sampling-without-replacement Chernoff
bound gives

\[
\Pr\left(K_p<\frac{\rho_0d}{2}\right)\le e^{-c_1d}.
\tag{3.3}
\]

Conditional on \(K_p=k\), the other \(k-1\) top targets are a uniform
sample without replacement from \(\mathcal T-\{T_e\}\).  The fraction of
rank-\(r\) targets containing \(x\) is

\[
\frac{\binom{n-1}{r-1}}{\binom n r}=\frac rn<\frac12.
\tag{3.4}
\]

Conditioning on \(T_e\ni x\) only decreases the remaining fraction.
Therefore

\[
\Pr(p\in E_x^{\rm top}\mid K_p=k)\le2^{-(k-1)}.
\tag{3.5}
\]

Equations (3.3)--(3.5) give the bound inside parentheses in (3.2) for
one \(p\).  There are \(d\) candidates in \(I_e\), so the union bound
proves (3.2).  Linearity of expectation gives the expected successful
incidence fraction.  Markov's inequality proves the high-probability
statement. \(\square\)

Random permutation is therefore not a plausible rounding mechanism for
the adaptive SCD pieces.  Its failure already occurs before lower targets,
owner envelopes, or the adjacency obstruction between companion pieces
are imposed.

## 4. The natural BTK/GMM chronology fails at positive density

The natural Greene--Kleitman/BTK chronology traverses each symmetric chain
monotonically and joins consecutive chains at alternating endpoints.
Let \(h,h'\) be the edge lengths of two chains meeting at an interface.
The BTK endpoint law gives

\[
|h-h'|=2
\tag{4.1}
\]

and a common active coordinate.  That coordinate is toggled once on each
chain.  If \(1\le h,h'\le d-1\), its two toggles lie in one
\(2d\)-edge window, so the projected Johnson chronology is not
\(d\)-resident.

### Theorem 4.1 (positive-density BTK interface failure)

At the triangular scale \(d^2/n\to\pi/8\), the natural cyclic BTK/GMM
ordering has at least

\[
\boxed{
\left(1-e^{-\pi/16}-o(1)\right)W}
\tag{4.2}
\]

interfaces with a repeated coordinate in a \(2d\)-edge window.

#### Proof

The number of BTK chains of edge length at least \(d\) is

\[
\binom n{\lfloor(n-d)/2\rfloor}.
\]

The local central-binomial estimate gives its ratio to the middle width
as

\[
\exp\left(-\frac{d^2}{2n}+o(1)\right)
\longrightarrow e^{-\pi/16}.
\tag{4.3}
\]

Chains of any fixed bounded positive length number \(o(W)\), and chains
whose lengths lie within two of the cutoff \(d\) also number \(o(W)\).
Hence
\[
\left(1-e^{-\pi/16}-o(1)\right)W
\]
chains have positive length at most \(d-3\).  By (4.1), the next chain
at their outgoing interface has length at most \(d-1\).  The common active
coordinate then repeats in a \(2d\)-edge window, proving (4.2).
\(\square\)

This is a no-go for the **natural** BTK/GMM chronology, not for every
ordering of the same SCD chains.  A new label-separated chain ordering
could evade it.

## 5. What a structured positive construction must prove

Theorem 2.1 suggests the correct SCD-side architecture.

1. Choose a structured SCD and order its rank-\((t-1)\) maxima in a
   cyclic \(d\)-resident sequence.
2. Put the delayed atoms (2.2) into the source positions.  This realizes
   every maximal target without a coordinate cover defect.
3. Assign the lower targets of each original or rephased SCD piece to
   shorter suffix intervals of the same atom word.
4. Prove that those shorter unions equal the prescribed SCD members, not
   merely subsets of their maxima.

Step 4 is the remaining nontrivial equality.  In coordinate form, for
every assigned target interval \(I\) with value \(X\), it is

\[
\boxed{
\begin{aligned}
x\in X&\Longrightarrow I
\text{ contains a \(d\)-window start whose envelope run contains \(x\)},\\
x\notin X&\Longrightarrow
\text{no selected source atom in \(I\) contains \(x\)}.
\end{aligned}}
\tag{5.1}
\]

Equivalently, with all positive and negative intervals included, every
positive interval must contain a point outside the union of the negative
intervals for that coordinate.

There is also an exact chronology constraint on the chosen SCD.  If a
\(d\)-safe Johnson successor \(P\) orders the top envelopes, its lower
flags are forced:

\[
L_j(T)=\bigcap_{i=0}^{j}P^iT.
\tag{5.2}
\]

Suppose an independently chosen SCD prescribes nested flags
\(L_j^\star(T)\), and complete them with corresponding upper flags to
induced middle maps \(R_j\).  The directed-history power-consistency
criterion gives

\[
\boxed{
\text{one endpoint chronology realizes all prescribed flags}
\quad\Longleftrightarrow\quad
R_j=R_1^j\ \ (0\le j\le d).}
\tag{5.3}
\]

Thus a BTK SCD cannot first be fixed as an unordered target partition and
then be made literal by an arbitrary Gray permutation of its maxima.
The SCD flags and the resident successor must be chosen simultaneously.
This is stronger than the run-length condition in Theorem 2.1.

The single-bulge and rank-two queue constructions prove (5.1) inside one
special component by designing the envelope runs first.  They do not
factor the complete named SCD target bank.  The next positive theorem is
therefore:

> **Resident SCD atom-factor theorem.**  There is a \(d\)-resident cyclic
> envelope ordering of the rank-\((t-1)\) targets whose delayed atoms
> realize, on the existing endpoint positions, all original and rephased
> SCD pieces with their prescribed suffix depths, equivalently with the
> power identities (5.3).

The random and natural BTK tests above show that this theorem requires a
deliberate residence construction; neither generic permutation nor the
standard recursive chain order is close to sufficient.
