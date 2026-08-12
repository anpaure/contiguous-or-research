# Abstract pairwise-pseudorandom rotor fibres can fail upper Hall identically

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, solver, or external input

## 0. Outcome

Use the truncated carrier-rotor parameters

\[
 M=m+H,\qquad a=H-Q,\qquad K=\left\lceil\frac{MN_H}{N_Q}\right\rceil,
\qquad c=Ka.
\]

There is an exact one-round distribution with the following properties.

1. Every realization is a collection of legitimate radius-\(Q\) rotor
   states.
2. Its current owners are distinct, and its next-owner candidate families
   are pairwise disjoint.
3. The labels of its two possible common upper stars are not merely
   pairwise independent: every proper subfamily of the labels is jointly
   independent and uniform.
4. Nevertheless every realization violates capacitated Hall in the
   depth-\(Q\) upper row.

Thus no implication based only on pairwise, or even proper-subfamily,
pseudorandomness of abstract upper-star labels can prove the simultaneous
round extension.

This is a proof-method obstruction, not a counterexample to the truncated
rotor path theorem.  The distribution varies which carrier from each
indexed pair supplies the bad state, and it does not show that such a fibre
is forced along one fixed all-carrier temporal trajectory.  In fact the
exact propagation identities give a stronger exclusion: after a
collision-free controlled layer, the bases of the next arrival stars are
distinct current adjacent flags.  Every common-star fibre constructed here
has repeated base \(U_{Q-1}=B\), so it cannot be the immediate successor
problem of such a layer.  The obstruction therefore closes abstract
pairwise-label and averaged-codegree arguments, but not the propagated
distinct-base facet-congestion lane.

There is also a fully fixed-catalogue packing statement.  If

\[
 s=Ka+1,
\]

then the carrier catalogue has a carrier-disjoint packing of bad
common-star blocks which covers at least

\[
 \left(1-\frac{s-1}{m-H+1}\right)N_H
\]

carriers.  Its number of blocks is \((1-o(1))N_H/s\).  The designated
identical-star pairs in this packing form only an \(O(s/m^2)=o(1)\)
fraction of all adjacent carrier pairs.  Moreover the block stars can be
chosen so that the average pairwise upper-star intersection over the
covered carriers is \(o(1)\).  Hence averaged pairwise codegree control
cannot exclude Hall failure; a uniform maximum-star-load invariant is
genuinely stronger.

## 1. Two actual upper stars with perfect owner separation

Put

\[
 n=2c=2Ka,\qquad d=m-H+1.
\]

At the TRP scale,

\[
 K=(\log m)^{1+o(1)},\qquad
 a=m^{1/2}(\log m)^{1/2+o(1)},
\]

so

\[
 n=o(m),\qquad n\le d
\]

for all sufficiently large \(m\).  Also

\[
 \binom{m+Q-2}{Q-1}\ge n.                         \tag{1.1}
\]

Choose sets \(B_0,B_1\subset[2m]\) satisfying

\[
 |B_0|=|B_1|=m+Q-1,\qquad
 |B_0\cap B_1|=2Q-2.
\]

Then

\[
 B_0\cup B_1=[2m].
\]

Choose

\[
 R_0\subset B_1\setminus B_0,\qquad
 R_1\subset B_0\setminus B_1,
\qquad |R_0|=|R_1|=a,
\]

and put

\[
 P_g=B_g\cup R_g\qquad(g=0,1).
\]

Each \(P_g\) has size \(M-1\), and

\[
 |[2m]\setminus P_g|=d.
\]

Choose, for every \(g\), distinct elements

\[
 e_{1,g},\ldots,e_{n,g}\in[2m]\setminus P_g
\]

and carriers

\[
 U_{i,g}=P_g\cup\{e_{i,g}\}.
\]

The two carrier pools are disjoint: a carrier in both would contain
\(P_0\cup P_1=[2m]\), impossible because \(M<2m\).

Fix \(w_g\in B_g\).  By (1.1), choose distinct \((m-1)\)-sets

\[
 C_{i,g}\subset B_g\setminus\{w_g\}.
\]

Apply the exact state construction from the common-upper-star theorem:
take \(z_Q=w_g\), put the other lower queue entries in \(C_{i,g}\), use
the \(Q-1\) points of \(B_g\setminus(C_{i,g}+w_g)\) for the upper queue,
put \(z_{2Q}=e_{i,g}\), and use \(R_g\) as the arrival reservoir.  This
gives a legitimate state on \(U_{i,g}\) with current owner

\[
 X_{i,g}=C_{i,g}+w_g,
\]

next-owner candidates

\[
 \{C_{i,g}+y:y\in R_g\},
\]

and depth-\(Q\) upper candidates

\[
 \mathcal F_g=\{B_g+y:y\in R_g\}.                 \tag{1.2}
\]

Within either group, the current owners are distinct and the next-owner
families are pairwise disjoint because the \(C_{i,g}\)'s are distinct and
\(B_g\cap R_g=\varnothing\).

The same holds across the two groups.  A common current owner would be an
\(m\)-set contained in \(B_0\cap B_1\), whose size is only \(2Q-2<m\).
If

\[
 C_{i,0}+y=C_{j,1}+y',
\]

then this \(m\)-set has at least \(m-1\) points in each \(B_g\), and
therefore at least \(m-2\) points in \(B_0\cap B_1\).  This is impossible
because \(2Q-2<m-2\).  Thus owner Hall holds with maximum slack in every
instance constructed below.

The two upper-star target families in (1.2) are also disjoint.  An equality

\[
 B_0+y=B_1+y'
\]

would produce a set containing \(B_0\cup B_1=[2m]\), although its rank is
only \(m+Q<2m\).

## 2. A proper-subfamily-independent distribution with certain Hall failure

Let

\[
 Z=(Z_1,\ldots,Z_n)
\]

be uniform on the parity class

\[
 \sum_{i=1}^n Z_i\not\equiv c\pmod2.              \tag{2.1}
\]

For any prescribed values of any \(n-1\) coordinates, there is exactly one
value of the remaining coordinate satisfying (2.1).  Consequently every
set of at most \(n-1\) coordinates is jointly uniform:

\[
 \Pr((Z_i)_{i\in J}=z)=2^{-|J|}
 \qquad(|J|\le n-1).                              \tag{2.2}
\]

In particular, the star labels are pairwise independent fair bits.

For one realization, select the \(n\) legitimate states

\[
 \omega_{i,Z_i}\quad(1\le i\le n)
\]

from Section 1.  Put

\[
 W_1=\sum_i Z_i,\qquad W_0=n-W_1.
\]

The parity condition gives \(W_1\ne c\).  Since \(n=2c\), either

\[
 W_1>c
\quad\text{or}\quad
 W_0>c.
\]

In the first case more than \(c\) carriers have the common candidate
family \(\mathcal F_1\); in the second, more than \(c\) carriers have
\(\mathcal F_0\).  Each family contains \(a\) targets, each of capacity
\(K\), so its total capacity is exactly

\[
 Ka=c.
\]

The overloaded group therefore violates capacitated Hall in every
realization.  The two disjoint stars have total capacity \(2c=n\), exactly
the number of selected carriers.  Thus this is not a trivial global
capacity deficit: the parity constraint excludes the unique balanced load
\((c,c)\).

This example is stronger than a pairwise-independence counterexample:
all proper-subfamily marginals agree exactly with independent fair labels.
The obstruction is the one global parity bit, which forces the two star
loads away from the only feasible balanced value.

The construction is made of actual rotor states.  What varies with \(Z\)
is the selected carrier \(U_{i,Z_i}\) in each indexed pair.  Equivalently,
one may put all \(2n\) carriers into a fixed catalogue, assign arbitrary
legitimate filler states to the unselected partners, and retain the
selected \(n\) carriers as the Hall witness.  This does not make the law a
stationary distribution on one fixed temporal TRP trajectory; that is why
the theorem is a proof-method limitation rather than an impossibility
result for TRP.

### 2.1 Exact temporal exclusion of the common-base fibre

For a state

\[
 \omega=(L;z_1,\ldots,z_{2Q};R),
\]

write

\[
 L_q(\omega)=L\cup\{z_1,\ldots,z_{Q-q}\},
 \qquad
 U_q(\omega)=L\cup\{z_1,\ldots,z_{Q+q}\}.
\]

If an arrival \(y\in R\) is used in the next transition, direct
substitution in the rotor recursion gives

\[
 X(\omega')=L_1(\omega)+y,
 \qquad
 L_q(\omega')=L_{q+1}(\omega)+y\quad(1\le q<Q),
 \tag{2.3}
\]

and

\[
 U_q(\omega')=U_{q-1}(\omega)+y\quad(1\le q\le Q).
 \tag{2.4}
\]

Thus, at every arrival-controlled row, the base of the successor star is
exactly a current adjacent flag.  In particular the depth-\(Q\) successor
star at carrier \(i\) is

\[
 \{U_{Q-1}(\omega_i)+y:y\in R_i\}.               \tag{2.5}
\]

If the controlled current flags are pairwise distinct across carriers,
then the bases in (2.5) are pairwise distinct.  But in each overloaded
group in Sections 1--2,

\[
 U_{Q-1}(\omega_{i,g})=B_g
\]

for every selected carrier of that group.  The group contains at least
\(c+1\ge2\) carriers, so it already has a collision in the
\(U_{Q-1}\)-row.  Consequently the parity-star obstruction cannot be the
immediate endpoint problem following a round which kept all controlled
flags collision-free.

The same argument applies block by block to Section 3: every block repeats
one \(U_{Q-1}\)-flag on \(s=c+1\) carriers.  Hence the packing below is a
packing in the unconstrained state catalogue, not in the temporally
propagated distinct-flag locus.  Notice also what the argument does *not*
give.  Distinct \((r-1)\)-bases may be distinct facets of one rank-\(r\)
target, so temporal distinctness excludes identical stars but does not
bound the maximum facet congestion of the distinct-base family.

## 3. An almost-spanning packing of actual common-star obstructions

Let

\[
 \mathcal U=\binom{[2m]}M,\qquad N=|\mathcal U|=N_H.
\]

Form an \(s\)-uniform hypergraph on \(\mathcal U\).  For every
\((M-1)\)-set \(P\), and every \(s\)-set
\(E\subset[2m]\setminus P\), include the block

\[
 \mathcal B(P,E)=\{P+e:e\in E\}.
\]

Every block supports the common-upper-star obstruction after splitting

\[
 P=B\sqcup R,\qquad |B|=m+Q-1,\quad |R|=a.
\]

The complement of every base \(P\) has size

\[
 d=2m-(M-1)=m-H+1.
\]

Take a maximal carrier-disjoint collection \(\mathscr M\) of the blocks
\(\mathcal B(P,E)\), and let \(\mathcal U_0\) be the set of uncovered
carriers.  Maximality has a strong consequence:

\[
 \#\{U\in\mathcal U_0:P\subset U\}\le s-1          \tag{3.1}
\]

for every \((M-1)\)-set \(P\).  Otherwise any \(s\) uncovered extensions
of \(P\) would form another block disjoint from \(\mathscr M\).

Double count the incidences

\[
 (P,U),\qquad P\subset U,\quad |P|=M-1,\quad
 U\in\mathcal U_0.
\]

Every uncovered carrier has exactly \(M\) lower faces.  The number of
\((M-1)\)-sets is

\[
 \binom{2m}{M-1}=\frac{NM}{d}.
\]

Using (3.1),

\[
 M|\mathcal U_0|
 \le (s-1)\binom{2m}{M-1}
 =\frac{(s-1)NM}{d}.
\]

Therefore

\[
 \boxed{
 |\mathcal U_0|\le\frac{s-1}{d}N.}                \tag{3.2}
\]

Since \(s=o(d)\), the maximal block packing covers \(1-o(1)\) of all
carriers.  If \(J=|\mathscr M|\), then

\[
 \boxed{
 \frac Ns\left(1-\frac{s-1}{d}\right)
 \le J\le\frac Ns,}
 \qquad
 J=(1-o(1))\frac Ns.                              \tag{3.3}
\]

This distinguishes the number of blocks, which is order \(N/s\), from
their carrier coverage, which is \(Js=(1-o(1))N\).

A base \(P\) may support several selected blocks.  Independently for each
block, choose a uniform \(a\)-subset \(R\subset P\), put \(B=P\setminus R\),
and use the upper star

\[
 \mathcal F(P,R)=\{B+y:y\in R\}.                  \tag{3.4}
\]

There are \(\binom{M-1}{a}\) possible decompositions.  We now verify that
some deterministic choice of these decompositions has vanishing average
pairwise star intersection.

Put

\[
 p=M-1,\qquad r=m+Q.
\]

For a fixed rank-\(r\) set \(S\subset P\), the event
\(S\in\mathcal F(P,R)\) occurs exactly when

\[
 R=(P\setminus S)\cup\{y\}
\]

for one of the \(r\) choices \(y\in S\).  Hence

\[
 \Pr_R(S\in\mathcal F(P,R))
 =\frac r{\binom p a}.                            \tag{3.5}
\]

For two distinct selected blocks, even if they have the same base,
independence and (3.5) give

\[
 \begin{aligned}
 \mathbb E|\mathcal F(P,R)\cap\mathcal F(P',R')|
 &=
 \binom{|P\cap P'|}{r}
 \left(\frac r{\binom p a}\right)^2\\
 &\le
 \binom p{a-1}
 \left(\frac r{\binom p a}\right)^2\\
 &=\frac{ar}{\binom p a}
 =:\varepsilon_m.
 \end{aligned}                                    \tag{3.6}
\]

Here

\[
 \varepsilon_m
 \le \frac{m^2}{\binom{M-1}{a}}
 =o(1).                                           \tag{3.7}
\]

Therefore there is a deterministic assignment of one decomposition to
each block for which the average cross-block star intersection is at most
\(\varepsilon_m\).

Choose the exact Theorem 5.1 states inside every block using those
decompositions.  Each block
violates upper Hall and has perfect owner Hall internally.  Repairing all
these carrier-disjoint Hall witnesses requires deleting at least one
carrier from every block, hence at least

\[
 J=(1-o(1))N/s
\]

carriers.

Write \(N_{\rm cov}=Js=(1-o(1))N\).  The number of designated pairs lying
in one common bad block is

\[
 J\binom s2=(1+o(1))\frac{N(s-1)}2.               \tag{3.8}
\]

Thus their density among all unordered carrier pairs is

\[
 (1+o(1))\frac{s}{N},
\]

which is exponentially small.  All designated pairs are adjacent in
\(J(2m,M)\).  The total number of adjacent carrier pairs is

\[
 \frac12 N M(m-H).
\]

Consequently their density among adjacent pairs is

\[
 \boxed{
 (1+o(1))\frac{s-1}{M(m-H)}
 =O\left(\frac{s}{m^2}\right)=o(1).}              \tag{3.9}
\]

More strongly, the deterministic decomposition assignment from (3.6)
satisfies

\[
 \begin{aligned}
 {1\over\binom{N_{\rm cov}}2}
 \sum_{\{U,V\}}
 |\mathcal F_U\cap\mathcal F_V|
 &\le
 {J\binom s2 a\over\binom{Js}2}+\varepsilon_m\\
 &=
 O\left(\frac{as}{N}\right)+\varepsilon_m
 =o(1).
 \end{aligned}                                    \tag{3.10}
\]

Thus even an almost-spanning state fibre can have vanishing average
pairwise upper-star codegree while containing order \(N/s\) disjoint exact
Hall witnesses.  A maximum star-load or higher-order fibre-expansion
invariant detects them.  By Section 2.1 this statement concerns the full
state catalogue; it is not an almost-spanning assertion inside a
collision-free propagated endpoint layer.

The packing still does not obstruct coefficient-one accounting.  One
deletion per block is only the fraction

\[
 \frac JN=(1+o(1))\frac1s=o(1)
\]

of a round.  No temporal theorem says that a nonvanishing deletion
fraction is forced over the \(M\) rounds.

## 4. Why a pairwise LLL cannot repair the obstruction

In one overloaded star, at least \(c+1\) carriers have only the \(a\)
upper targets in \(\mathcal F_g\), each of capacity \(K\).  Cloning every
target \(K\) times gives exactly

\[
 aK=c
\]

right slots.  There is no transversal for \(c+1\) left parts.  Therefore
the conflict-free event is empty under every product sampling law.

This is stronger than failure of a numerical local-lemma criterion:
conditioning on no conflicts is impossible.  At least one carrier must be
removed from each overloaded block before an LLL or independent
transversal can apply.

The parity-star distribution shows why pairwise probabilities cannot
certify otherwise.  They agree exactly with independent fair star labels
on every proper subfamily, while the unique global parity constraint makes
the Hall event impossible.  A successful temporal invariant must control
actual star loads or all Hall cuts, not merely pairwise collision
probabilities, covariances, or averaged conflict degree.

## 5. Exact boundary

Proved:

1. proper-subfamily independence of abstract upper-star labels does not
   imply one-round capacitated Hall;
2. the counterinstances use legitimate rotor states and retain perfect
   owner Hall on the Hall-witness family;
3. common-upper-star Hall witnesses admit an almost-spanning
   carrier-disjoint packing while their identical-star pairs remain an
   \(o(1)\) fraction even among adjacent carrier pairs;
4. no pairwise LLL can repair an overloaded block without deleting a
   carrier;
5. the exact rotor recursion excludes every common-base obstruction in
   this note from the immediate successor problem of a collision-free
   controlled layer.

Not proved:

1. that the parity-star instances arise along one fixed all-carrier rotor
   trajectory;
2. that any bad block is unavoidable under a global path selection;
3. that the required deletions have nonvanishing total cost over all
   rounds;
4. any analogous no-go on the propagated distinct-base locus;
5. failure of TRP.

The theorem therefore closes only the abstract pairwise-label and averaged
pairwise-codegree proof lane.  It does **not** close the propagated
distinct-base lane.  On that locus the residual obstruction is precisely
facet congestion: many different adjacent flags may be facets of the same
next target.  The needed replacement is a uniform distinct-base
facet-load/Hall-cut invariant propagated through time.
