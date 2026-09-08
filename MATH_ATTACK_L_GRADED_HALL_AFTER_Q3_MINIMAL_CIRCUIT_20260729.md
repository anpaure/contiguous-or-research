# Graded one-core Hall after positive lower q=3:
# the exact submodular dual and the first surviving circuits

Date: 2026-07-29

Status: theorem-grade reduction and sharp abstract obstruction.  For a fixed
equivariant one-core, weighted quotient Hall is exactly the nonnegativity of
a submodular block-set function.  Lower-q3 positive degree removes the
rank-five zero-degree floor but does not remove possible lower-rank zeros.
Conditional on every target orbit having positive degree, every
inclusion-minimal Hall obstruction is a connected no-private-block circuit
of exactly one of three numerical types, with defect 15, 5, or 3.  The
smallest possible survivor is a two-target rank-five-short circuit of
defect 3.  Positive degree, all aggregate rank cuts, Boolean-interval
columns, and local Johnson/one-core feasibility do not exclude this
circuit.

This note does not construct a global strict carrier satisfying lower q=2,
three-residence, all upper layers, and exhibiting such a circuit.
Accordingly it does not refute the desired implication from the full
carrier hypotheses to Hall.  It identifies the exact next obstruction and
shows that any proof of the implication must use some global compatibility
absent from submodularity, rank counts, and local interval geometry.  The
common same-row chronology is the natural available source of that extra
compatibility.

## 1. The weighted quotient graph

Fix

\[
 k=15,\qquad d=3,\qquad r=8,\qquad h=r-d=5,
\]
\[
 W={15\choose 8}=6435,\qquad N=W/15=429.
\tag{1.1}
\]

Let \(P=(P_i)_{i\in\mathbb Z_W}\) be the rank-five erosion controller of a
strict equivariant three-resident rank-eight carrier, and let
\(C=(C_i)\) be a fixed equivariant one-core:

\[
 C_i\subseteq P_i,\qquad DC=DP,\qquad
 (DX)_i=X_i\cup X_{i+1}.
\tag{1.2}
\]

The cyclic equivariance has 429 free position orbits.  Denote their set by
\(\mathcal J\).  Every \(J\in\mathcal J\) contains 15 physical positions
and therefore has quotient capacity 15.

Let \(\mathcal O\) be the set of cyclic target orbits of nonempty subsets
of \(\mathbb Z_{15}\) of rank at most five.  A target orbit \(O\) is
adjacent to \(J\) when some compatible phases have

\[
                         C_i\subseteq S\subseteq P_i,
\qquad S\in O,\quad i\in J.
\tag{1.3}
\]

Write this quotient neighborhood as \(N_C(O)\).  The target demand is its
physical orbit size \(w(O)\).  The orbit census is

\[
\begin{array}{c|c|c}
 |S| & \text{target-orbit census} & \text{total demand}\\ \hline
 1 & 15^1 & 15\\
 2 & 15^7 & 105\\
 3 & 15^{30}+5^1 & 455\\
 4 & 15^{91} & 1365\\
 5 & 15^{200}+3^1 & 3003 .
\end{array}
\tag{1.4}
\]

Thus there are 331 target orbits, of total weight

\[
                         4943=\sum_{s=1}^5{15\choose s}.
\tag{1.5}
\]

The weighted quotient Hall condition is

\[
       w(X):=\sum_{O\in X}w(O)
       \ \le\ 15\,|N_C(X)|
       \qquad\text{for every }X\subseteq\mathcal O.
\tag{1.6}
\]

The quotient construction and its physical lift are taken from the
audited graded-compiler reduction.  This note attacks only (1.6).

## 2. Exact submodular block-set dual

For a set \(B\subseteq\mathcal J\) of right orbits, define its closed
target shore

\[
             Y_C(B):=\{O\in\mathcal O:N_C(O)\subseteq B\}
\tag{2.1}
\]

and its block deficit function

\[
             \Phi_C(B):=
             15|B|-\sum_{O\in Y_C(B)}w(O).
\tag{2.2}
\]

Also define the maximum weighted Hall defect

\[
 \eta(C):=\max_{X\subseteq\mathcal O}
          \bigl(w(X)-15|N_C(X)|\bigr).
\tag{2.3}
\]

The empty target shore shows \(\eta(C)\ge0\).

### Theorem 2.1 (exact block-set dual)

For every fixed equivariant one-core \(C\),

\[
                         \eta(C)=-\min_{B\subseteq\mathcal J}\Phi_C(B).
\tag{2.4}
\]

Consequently the quotient graph satisfies weighted Hall if and only if

\[
                         \Phi_C(B)\ge0
                         \quad\text{for every }B\subseteq\mathcal J.
\tag{2.5}
\]

Moreover, \(\Phi_C\) is submodular:

\[
 \Phi_C(B_1)+\Phi_C(B_2)
 \ge
 \Phi_C(B_1\cap B_2)+\Phi_C(B_1\cup B_2).
\tag{2.6}
\]

#### Proof

For a fixed \(B\), put \(X=Y_C(B)\).  Since \(N_C(X)\subseteq B\),

\[
 \eta(C)\ge w(Y_C(B))-15|N_C(Y_C(B))|
          \ge w(Y_C(B))-15|B|
          =-\Phi_C(B).
\tag{2.7}
\]

Conversely, for an arbitrary \(X\), put \(B=N_C(X)\).  Then
\(X\subseteq Y_C(B)\), and hence

\[
 -\Phi_C(B)
 =w(Y_C(B))-15|B|
 \ge w(X)-15|N_C(X)|.
\tag{2.8}
\]

Taking the two maxima proves (2.4), and (2.5) follows.

For a fixed target orbit \(O\), the indicator

\[
                         {\bf1}_{N_C(O)\subseteq B}
\tag{2.9}
\]

is supermodular as a function of \(B\).  Indeed, the only nontrivial case
is when \(N_C(O)\) is contained in \(B_1\cup B_2\) but in neither
\(B_1\) nor \(B_2\); then the right side of the supermodular inequality is
one and the left side is zero.  Therefore (2.2), a modular function minus
a positive weighted sum of supermodular indicators, is submodular.
\(\square\)

### Corollary 2.2 (uncrossing)

The minimizers of \(\Phi_C\) are closed under union and intersection.  In
particular there is a unique least minimizing block set and a unique
greatest minimizing block set.

#### Proof

If \(B_1,B_2\) both attain the minimum \(\mu\), submodularity gives

\[
 2\mu\ge\Phi_C(B_1\cap B_2)+\Phi_C(B_1\cup B_2)\ge2\mu.
\]

Thus both new sets are minimizers.  Iterating gives the least and greatest
ones.  \(\square\)

This is the useful force of submodularity: a bad target shore can be
replaced by a canonical closed block shore.  Submodularity alone does not
make its minimum nonnegative.

## 3. Removing the lower-q3 zero-degree floor

Let

\[
                  Z:=\{O\in\mathcal O:N_C(O)=\varnothing\}.
\tag{3.1}
\]

For rank five, containment in (1.3) reduces to equality:

\[
 |S|=|P_i|=5,\qquad S\subseteq P_i
 \quad\Longleftrightarrow\quad S=P_i.
\tag{3.2}
\]

Thus lower-q3 positive degree is exactly the assertion that no rank-five
target orbit lies in \(Z\); it is independent of the choice of \(C\).
It does not say that a positive rank-five orbit has enough distinct
neighbors to avoid a joint Hall circuit.

Nor does it exclude a zero-degree target of rank at most four for the
chosen core.  Such a target is an earlier Hall obstruction than the
positive-degree circuits classified below.  In particular, the singleton
orbit has positive degree for some equivariant one-core if and only if
some forced port has size one; see Section 7.

Define the residual block function

\[
 \Phi_C^+(B):=
 15|B|-
 \sum_{\substack{O\notin Z\\N_C(O)\subseteq B}}w(O).
\tag{3.3}
\]

Since every zero orbit is closed inside every \(B\),

\[
 \Phi_C(B)=\Phi_C^+(B)-w(Z),
\qquad
 \eta(C)=w(Z)-\min_B\Phi_C^+(B).
\tag{3.4}
\]

If all target orbits have positive degree, then \(Z=\varnothing\), and the
whole remaining question is exactly

\[
                         \min_B\Phi_C^+(B)=0.
\tag{3.5}
\]

### Exact calibration on the residence seed

For the canonical core of the audited artifact

  scratch/fixtures/k15_residence_hint_explicit_v1.json

with SHA-256

  4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10,

the missing rank-five orbit representatives are

\[
\begin{split}
157,\ 285,\ 651,\ 661,\ 665,\ 837,\ 1187,\ 1233,\ 1349,\ 1585,\ 2329.
\end{split}
\tag{3.6}
\]

All eleven have full weight 15.  Hence

\[
                         w(Z)=11\cdot15=165.
\tag{3.7}
\]

The exact weighted quotient flow and the exact physical matching both
have value

\[
                         4778=4943-165.
\tag{3.8}
\]

The residual source-reachable shore returned by the canonical max-flow
consists exactly of the eleven zero-degree rank-five orbits, and

\[
                         \min_B\Phi_C^+(B)=0.
\tag{3.9}
\]

Thus this canonical core has no additional Hall deficiency beyond the
missing lower-q3 targets.  This is an exact calibration, not a proof for
all cores or for a repaired carrier.  In particular, the residence seed
itself misses 47 lower-q2 orbits and upper orbits in ranks 9, 10, and 11,
so it is not a counterexample to the full implication under study.

The minimum Hall shore is not unique.  There are also 53 balanced full
rank-five quotient packets of demand 15 having one capacity-15 neighbor;
adjoining any selection of these tight packets to the eleven zero orbits
preserves defect 165.  This does not create residual deficiency after the
zero orbits are removed.

## 4. Classification of every minimal positive-degree obstruction

For \(X\subseteq\mathcal O\), write

\[
                         \Delta_C(X):=w(X)-15|N_C(X)|.
\tag{4.1}
\]

Assume from now on that every target orbit in \(X\) has positive degree,
and choose \(X\) inclusion-minimal subject to

\[
                         \Delta_C(X)>0.
\tag{4.2}
\]

### Theorem 4.1 (minimal circuit theorem)

Every such \(X\) has the following properties.

1. Its induced target-right incidence graph is connected.

2. No right orbit is private to one target orbit of \(X\).  Equivalently,
   every \(J\in N_C(X)\) is adjacent to at least two members of \(X\).

3. For every \(O\in X\),

\[
                         0<\Delta_C(X)\le w(O).
\tag{4.3}
\]

4. Exactly one of the following three mutually exclusive cases occurs:

\[
\begin{array}{c|c|c}
\text{type}&\text{short target orbits in }X&\Delta_C(X)\\ \hline
F&\text{none}&15\\
E_3&\text{the unique rank-three orbit of weight }5&5\\
E_5&\text{the unique rank-five orbit of weight }3&3.
\end{array}
\tag{4.4}
\]

The two short target orbits cannot occur together in a minimal deficient
shore.

#### Proof

If the induced incidence graph were disconnected, its target components
would have disjoint right neighborhoods, so \(\Delta_C(X)\) would be the
sum of their defects.  At least one proper component would have positive
defect, contradicting inclusion minimality.  This proves part 1.

For \(O\in X\), let

\[
 p_O:=
 |N_C(O)\setminus N_C(X\setminus\{O\})|
\tag{4.5}
\]

be the number of right orbits private to \(O\).  Direct subtraction gives

\[
 \Delta_C(X\setminus\{O\})
 =
 \Delta_C(X)-w(O)+15p_O.
\tag{4.6}
\]

All target weights are at most 15.  If \(p_O\ge1\), the right side is at
least \(\Delta_C(X)>0\), again contradicting minimality.  Thus \(p_O=0\)
for every \(O\), proving part 2.  Equation (4.6) and minimality now give
(4.3).

Let \(f\) be the number of full weight-15 orbits in \(X\), let
\(\epsilon_3\) record membership of the unique weight-5 rank-three orbit,
let \(\epsilon_5\) record membership of the unique weight-3 rank-five
orbit, and put \(b=|N_C(X)|\).  Then

\[
 \Delta_C(X)
 =15(f-b)+5\epsilon_3+3\epsilon_5.
\tag{4.7}
\]

If both exceptional orbits are absent, (4.3) and congruence modulo 15
force \(\Delta_C(X)=15\).  If only the rank-three exceptional orbit is
present, (4.3) gives \(0<\Delta_C(X)\le5\), while (4.7) is congruent to
5 modulo 15; hence the defect is 5.  If only the rank-five exceptional
orbit is present, the same argument gives defect 3.  If both are present,
(4.3) would give a positive integer at most 3 that is congruent to
8 modulo 15, which is impossible.  This proves part 4.  \(\square\)

### Corollary 4.2 (the next minimal obstruction)

Under positive degree, an inclusion-minimal deficient shore has at least
two target orbits.  The smallest possible defect is 3.  Its smallest
possible support has the form

\[
 \{\text{one full orbit of weight }15,\ 
   \text{the exceptional rank-five orbit of weight }3\}
\tag{4.8}
\]

with a single common right orbit and no other neighbor.  Its demand is 18
against capacity 15.

Likewise the smallest type \(E_3\) circuit has demands \(15+5\) on one
right orbit, and the smallest type \(F\) circuit has demands \(15+15\) on
one right orbit.

#### Proof

Positive degree gives \(b\ge1\).  In type \(E_5\), (4.7) and defect 3
give \(f=b\), so \(b=f=1\) is the smallest case.  The other two cases are
identical: type \(E_3\) has \(f=b\), while type \(F\) has \(f=b+1\).
\(\square\)

This answers the numerical part of the question.  Lower-q3 positive degree
removes the isolated rank-five defect but leaves a possible defect-three
joint circuit.

## 5. Aggregate rank cuts and why they are not enough

Let

\[
 B_s(C):=\{J\in\mathcal J:|C_i|\le s
                   \text{ for the positions in }J\}.
\tag{5.1}
\]

Every target orbit of rank at most \(s\) has neighborhood contained in
\(B_s(C)\).  Therefore Hall implies

\[
 15|B_s(C)|\ge\sum_{t=1}^s{15\choose t}.
\tag{5.2}
\]

For \(s=1,2,3,4\), this is exactly

\[
 |B_1|\ge1,\qquad |B_2|\ge8,\qquad
 |B_3|\ge39,\qquad |B_4|\ge130.
\tag{5.3}
\]

These are block-dual cuts, but only the coarsest ones.  Once (5.3) passes,
a bad minimizer can still be label-sensitive: a proper family of target
orbits can be trapped in too few Boolean intervals even though the total
capacity at every core-rank threshold is adequate.

### Proposition 5.1 (exact ranks-one-and-two diversity test)

Suppose

\[
                         |B_1|=1,\qquad |B_2|=8,
\tag{5.4}
\]

and the singleton target orbit has positive degree.  Hall restricted to
target ranks one and two holds if and only if the seven right orbits with
core rank exactly two represent the seven distinct cyclic pair-difference
orbits.

#### Proof

The singleton orbit has weight 15 and can use only the unique member of
\(B_1\), so that right orbit's entire capacity is required by rank one.
A rank-two target can use a core-rank-two right orbit only when its target
equals that core.  Thus each of the remaining seven right orbits supplies
capacity only to its own cyclic pair-difference type.  Necessity follows.
If all seven types occur, assign the singleton orbit to the member of
\(B_1\) and each rank-two orbit to its corresponding core-rank-two right
orbit.  This gives the required restricted matching.  \(\square\)

Thus even the first nontrivial rank layer already needs orbit-type
diversity, a relational datum invisible in (5.3).

## 6. A sharp Boolean-interval obstruction

The following construction is deliberately an abstract quotient interval
table.  It proves that positive degree, the exact rank counts (5.3), and
local one-core chart feasibility do not imply Hall.  It is not asserted
to arise from one global strict cyclic carrier.

Let

\[
                         Q=\{0,3,6,9,12\}.
\tag{6.1}
\]

Its translation orbit is the exceptional rank-five orbit of weight 3.
Make one right orbit \(J_*\) with Boolean interval

\[
                         [C,P]=[\{0\},Q].
\tag{6.2}
\]

Then \(J_*\) is adjacent to the singleton target orbit \(U\), of weight
15, and to the exceptional orbit \(E_5\), of weight 3.

For every other target orbit \(O\), choose a representative \(S\) and
give it one designated private right orbit with

\[
                         C=S,\qquad S\subseteq P,\qquad |P|=5.
\tag{6.3}
\]

If \(|S|=5\), take \(P=S\).  If \(|S|\le4\), choose a rank-five
superset \(P\) outside the orbit of \(Q\).  Such a choice always exists:
even for \(|S|=4\), there are 11 rank-five supersets of \(S\), whereas
the whole exceptional orbit contains only three sets.  Choose these
columns so that neither \(U\) nor \(E_5\) gets an additional neighbor.
Finally add 99 filler right orbits with \(C=P\) of rank five, again
outside the exceptional orbit.

There are

\[
 1+(7+31+91+200)+99=429
\tag{6.4}
\]

right orbits.  All 331 target orbits have positive degree.  The cumulative
core-rank counts are exactly

\[
                         b_1=1,\quad b_2=8,\quad
                         b_3=39,\quad b_4=130.
\tag{6.5}
\]

Thus every aggregate rank screen (5.3) passes.  Nevertheless

\[
                         N(U)=N(E_5)=\{J_*\},
\tag{6.6}
\]

so

\[
 \Delta(\{U,E_5\})=15+3-15=3.
\tag{6.7}
\]

This realizes the sharp type \(E_5\) circuit from Corollary 4.2.

### Lemma 6.1 (each column is locally one-core realizable)

Every nonempty Boolean interval \([C,P]\) used above, with
\(C\subseteq P\) and \(|P|=5\), occurs as the center of a strict
three-position Johnson chart satisfying \(DC=DP\) on both incident
edges.

#### Proof

Choose \(a,b\in C\), allowing \(a=b\), and distinct or arbitrary labels
\(u,v\notin P\).  Put

\[
 P^-=(P-\{a\})\cup\{u\},\qquad
 P^+=(P-\{b\})\cup\{v\},
\tag{6.8}
\]

and choose neighboring cores

\[
                         C^-=P^-,\qquad C^+=P^+.
\tag{6.9}
\]

Both \(P^-\!-\!P\) and \(P\!-\!P^+\) are strict Johnson edges.  Since
\(a,b\in C\),

\[
 C^-\cup C=P^-\cup P,\qquad
 C\cup C^+=P\cup P^+.
\tag{6.10}
\]

These are exactly the two local equations \(DC=DP\).  \(\square\)

The obstruction therefore survives Boolean interval structure and every
radius-one one-core test.  What is missing from the construction is a
single global chronology that simultaneously supplies all columns,
lower-q2 completeness, three-residence, and upper completeness.  Any
positive theorem must use that missing compatibility.

## 7. Envelope, forced-port, and chosen-core cuts

At a controller position define the forced port

\[
 F_i:=(P_i\setminus P_{i-1})\cup
      (P_i\setminus P_{i+1}).
\tag{7.1}
\]

Every one-core satisfying \(DC=DP\) obeys

\[
                         F_i\subseteq C_i\subseteq P_i.
\tag{7.2}
\]

For a target orbit \(O\), define three quotient neighborhoods:

\[
\begin{aligned}
N_P(O)&=\{J:\text{some phases have }S\subseteq P_i\},\\
N_F(O)&=\{J:\text{some phases have }F_i\subseteq S\subseteq P_i\},\\
N_C(O)&=\{J:\text{some phases have }C_i\subseteq S\subseteq P_i\}.
\end{aligned}
\tag{7.3}
\]

Then

\[
                         N_C(O)\subseteq N_F(O)\subseteq N_P(O).
\tag{7.4}
\]

Let \(\Phi_P,\Phi_F,\Phi_C\) be the block functions (2.2) made from these
three neighborhood systems.  Pointwise in \(B\),

\[
                         \Phi_C(B)\le\Phi_F(B)\le\Phi_P(B).
\tag{7.5}
\]

Hence the remaining obstruction hierarchy is exact:

1. If \(\Phi_P(B)<0\), the controller envelope itself fails and no
   one-core can repair it.

2. If \(\Phi_P\ge0\) but \(\Phi_F(B)<0\), the mandatory endpoint ports
   fail and no one-core can repair it.

3. If \(\Phi_F\ge0\) but \(\Phi_C(B)<0\), the failure is due to the
   globally chosen run phases or additional core letters.

A singleton has a forced-port candidate exactly when some
\(|F_i|=1\).  In the run language this is a length-one \(P\)-run, or
equivalently a length-four positive run in the depth-three dilation
\(T=D^3P\).  The presently stated carrier gates do not by themselves
provide a proved lower bound on the distribution of such ports.

Lower-q2 completeness says that every rank-six target occurs as
\(P_i\cup P_{i+1}\), a union of adjacent rank-five facets.  It does not
directly imply that a prescribed lower target lies in either facet: a
set containing both coordinates unique to the two facets lies in neither.
Upper completeness constrains unions along the middle chronology, but no
general implication from those upper unions to nonnegativity of
\(\Phi_P\) or \(\Phi_F\) is currently proved.

## 8. Exact proved boundary and the remaining theorem

The following statements are proved.

1. For every fixed equivariant one-core, weighted Hall is equivalent to
   nonnegativity of the submodular block function \(\Phi_C\).

2. Lower-q3 positive degree removes every rank-five zero orbit, but does
   not remove possible lower-rank zeros or joint circuits.

3. Every inclusion-minimal positive-degree obstruction is connected,
   has no private right block, and has exact defect 15, 5, or 3 according
   to (4.4).

4. The first numerical obstruction is the defect-three type \(E_5\)
   circuit.  Positive degree, all aggregate rank cuts, Boolean interval
   columns, and local Johnson/one-core charts do not exclude it.

5. In the canonical residence seed, the whole deficiency 165 is exactly
   the eleven missing full rank-five orbits.  Its canonical core has no
   residual deficient circuit.

What is not proved is the global assertion

\[
\begin{split}
 &\text{strict equivariant three-residence}
 +\text{ lower-q2 completeness}
 +\text{ upper completeness}
 +\text{ lower-q3 positive degree}\\
 &\hspace{35mm}\Longrightarrow
 \exists\,C\subseteq P,\ DC=DP,\ 
 \Phi_C(B)\ge0\ \text{for every }B.
\end{split}
\tag{8.1}
\]

Two exact chronology-sensitive completion targets are the following.

### Forced-port expansion form

\[
 \Phi_F(B)\ge0\quad\text{for every }B\subseteq\mathcal J,
\tag{8.2}
\]

together with a run-phase selection theorem producing a one-core \(C\)
for which shrinking \(N_F\) to \(N_C\) creates no negative block cut.

### Minimal-circuit exclusion form

For every globally legal carrier, there is an equivariant one-core \(C\)
for which every target orbit has positive degree and no connected
no-private-block target family of type \(F\), \(E_3\), or \(E_5\) exists.

Equation (8.2) is the cleaner carrier-only target.  It must first make
every forced-port target neighborhood nonempty.  After that unary gate,
the defect-three \(E_5\) circuit is the first numerical joint obstruction.
A proof based only on submodularity or interval-by-interval feasibility
cannot exclude it; it needs an additional global relation linking the 429
columns, for which the common cyclic chronology is the intended candidate.
