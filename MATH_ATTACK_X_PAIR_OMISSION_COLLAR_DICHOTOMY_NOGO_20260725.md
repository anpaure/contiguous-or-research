# Pair-omission collar dichotomy: legal owner-fixed spikes and a sharp chronology no-go

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
web search is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad
W=\binom{2m+1}{m},\qquad
T=\binom{2m+1}{m-1},
\]

and

\[
A_m=\binom{2m-1}{m-1},\qquad
R_m=\frac{A_m}{2m-1}=\operatorname {Cat}_{m-1}.
\]

The requested local conclusion

\[
\text{constant-fraction pair charge with cost }
O\!\left(\frac{tq}{m}\right)
\tag{0.1}
\]

is false. It already fails at \(q=1\) inside a genuine exact factor and a
literal pair-omission matching.

The strongest true local statement is the following.

> **Owner-fixed spike theorem.** Let \(t\) actual occurrences in one exact
> phase factor have the same upper depth-\(q\) target \(U\), where
> \(1\le q\le H\le m-2\). One may choose a star-compatible family of exact
> partner factors and, for every occurrence, a literal alternate which
> fixes its lower endpoint, its middle owner, and every lower flag.
> Arbitrary simultaneous choices remain one integral central matching.
> At the target depth the joined Gram charges all
> \(\binom t2\) old collision pairs. Moreover, there is a literal corner
> whose new internal \(U\)-spike collision count is at most
> \[
> \frac1q\binom t2
> \]
> for \(q\ge2\), while at \(q=1\) it is zero. Thus at least one half of
> the internal spike is literally burned at every depth, and every
> internal pair is burned at depth one. The released-root count is exactly
> zero.

Its unavoidable defect is chronology, not ownership. In the standard
fixed-partition extraction, a depth-one spike can be arranged so that no
fixed partner chart sees even one of its collision pairs. Any independently
paid one-\(U\) literal partner-spike repair, with no auxiliary cross-\(U\)
filler insertion, which charges a fixed fraction \(\delta>0\) must then pay

\[
\Omega_\delta(t)
\tag{0.2}
\]

released lower roots or new source-row runs. This contradicts (0.1), since at
\(q=1\) the proposed cost is \(O(t/m)\).

There are two further scope barriers.

1. Positive joined Gram is curvature between two coherent endpoints; by
   itself it does not imply descent from the current load profile.
2. Paying the spikes independently over upper targets does not aggregate
   to \(o(W/H)\). At Gaussian depth there is
   \(\Theta(W)\) repeated-occurrence mass, so even the hoped-for formal
   rate \(tq/m\) sums only to the boundary order \(W/H\), not little-\(o\).

Thus the collar gate is closed in its proposed targetwise form. The only
remaining escape is a genuinely cross-\(U\), cross-row literal braid which
shares physical carriers between many different upper targets, together
with a load-oriented recentering theorem. Neither is supplied by collar
intersection or partner averaging.

No coefficient-one theorem is claimed.

## 1. Exact local notation

Fix an omitted pair

\[
A=\{a,b\}\subset[n],\qquad Q_A=[n]\setminus A,
\]

and an exact cyclic row factor \(F_A\) on \(Q_A\). Write a row as

\[
\pi=(x_0,\ldots,x_{2m-2})
\]

with cyclic indices. A token at start \(i\) has

\[
S_i=I_\pi(i,m-1),\qquad
Y_i=I_\pi(i-1,m),
\tag{1.1}
\]

and upper flags

\[
U_p(i)=I_\pi(i-1,m+p),\qquad 1\le p\le H.
\tag{1.2}
\]

Suppose distinct selected token edges \(e_1,\ldots,e_t\) in an existing
lower-saturating, middle-injective central matching have one common
depth-\(q\) upper target

\[
U_q(e_i)=U,\qquad |U|=m+q.
\tag{1.3}
\]

Put

\[
C_i=U\setminus S_i,\qquad |C_i|=q+1.
\tag{1.4}
\]

The distinguished predecessor collar coordinate is

\[
p_i=Y_i\setminus S_i,
\tag{1.5}
\]

and the owner-inert right-suffix collar is

\[
D_i=C_i\setminus\{p_i\},\qquad |D_i|=q.
\tag{1.6}
\]

Thus

\[
Y_i=S_i\cup\{p_i\},
\]

whereas every coordinate of \(D_i\) lies strictly after \(Y_i\) in the
source row.

Every assertion below is integral in the following precise sense. For one
fixed partner pair \(B\), one bijection \(B\to A\), one permutation
\(\theta_B\), and one exact factor

\[
F_B=\theta_BF_A
\tag{1.7}
\]

are frozen globally. Occurrence-dependent choices of the bijection for the
same \(B\) are not allowed.

## 2. Exact common-partner census

Let

\[
E=Q_A\setminus U,\qquad |E|=d=m-q-1.
\tag{2.1}
\]

For a pair \(B\in\binom{Q_A}{2}\), let \(\theta_B\) exchange \(B\) with
\(A\). Call occurrence \(i\) lower-active for \(B\) when \(\theta_B\)
fixes \(S_i\) and changes \(U\).

### Lemma 2.1 (exact eligibility)

Occurrence \(i\) is lower-active for \(B\) if and only if

\[
\varnothing\ne B\cap U\subseteq C_i.
\tag{2.2}
\]

It is additionally middle-owner inert if and only if

\[
\varnothing\ne B\cap U\subseteq D_i.
\tag{2.3}
\]

Two occurrences \(i,j\) are simultaneously lower-active if and only if

\[
\varnothing\ne B\cap U\subseteq C_i\cap C_j.
\tag{2.4}
\]

#### Proof

Because \(A\) is disjoint from every old source-row set, \(\theta_B\)
fixes \(S_i\) precisely when \(B\cap S_i=\varnothing\). Since

\[
S_i=U\setminus C_i,
\]

and \(\theta_B\) changes \(U\) precisely when \(B\cap U\ne\varnothing\),
these two conditions are equivalent to (2.2).

The owner is

\[
Y_i=S_i\cup\{p_i\}.
\]

Therefore it is fixed precisely when the part of \(B\) lying in \(U\)
avoids both \(S_i\) and \(p_i\), which is (2.3). Intersecting the
conditions for \(i\) and \(j\) gives (2.4). \(\square\)

Consequently collar intersection is exactly the containment criterion for
an arbitrary common partner. If \(C_i\cap C_j\ne\varnothing\), choose

\[
c\in C_i\cap C_j,\qquad y\in E,
\]

and take \(B=\{c,y\}\). The helper \(y\) exists because \(q\le m-2\).
For a frozen extraction partition this is not sufficient: the pair \(B\)
must also be in the available partner menu, its factor must satisfy
(1.7), and the associated priority/background chart must be legal.

### Lemma 2.2 (exact all-partner counts)

One occurrence is lower-active for exactly

\[
\alpha_q
=(q+1)d+\binom{q+1}{2}
=\frac{(q+1)(2m-q-2)}2
\tag{2.5}
\]

partner pairs. It is middle-owner inert for exactly

\[
\alpha_q^0
=qd+\binom q2
=\frac{q(2m-q-3)}2
\tag{2.6}
\]

partners. Their difference is exactly

\[
\alpha_q-\alpha_q^0=m-1.
\tag{2.7}
\]

If

\[
h_{ij}=|C_i\cap C_j|,
\]

then the collision pair \(\{i,j\}\) is lower-active in exactly

\[
\beta(h_{ij})=dh_{ij}+\binom{h_{ij}}2
\tag{2.8}
\]

partner charts.

If \(a_B\) denotes the number of lower-active occurrences for \(B\), and

\[
d_x=\#\{i:x\in C_i\},\qquad
d_{xy}=\#\{i:\{x,y\}\subseteq C_i\},
\]

then

\[
\sum_B a_B=t\alpha_q
\tag{2.9}
\]

and

\[
\boxed{
\sum_B\binom{a_B}{2}
=d\sum_{x\in U}\binom{d_x}{2}
+ \sum_{\{x,y\}\subset U}\binom{d_{xy}}2.}
\tag{2.10}
\]

The owner-inert analogues are obtained by replacing \(C_i\) by \(D_i\)
and \(\alpha_q\) by \(\alpha_q^0\).

#### Proof

An active pair \(B\) is a two-subset of \(C_i\cup E\) not wholly
contained in \(E\). It either has one point in each set or two points in
\(C_i\), which gives (2.5). Replacing \(C_i\) by \(D_i\) gives (2.6);
subtraction gives (2.7).

For two occurrences, the same argument uses

\[
Q_A\setminus(S_i\cup S_j)=E\cup(C_i\cap C_j),
\]

giving (2.8). Summing (2.8) over \(i<j\) and double-counting common
collar points and common collar pairs proves (2.10). \(\square\)

The fraction of all partner pairs which activates one occurrence is

\[
\frac{\alpha_q}{\binom{2m-1}{2}}
=\frac{(q+1)(2m-q-2)}
       {2(2m-1)(m-1)}
=\left(1+O\!\left(\frac qm\right)\right)\frac{q+1}{2m}.
\tag{2.11}
\]

This is the source of the tempting \(tq/m\) average. Equation (2.10)
shows why that average is not a collision-effective chronology bound.
If the collars are disjoint, every term in (2.10) is zero. At the other
extreme, in a sunflower \(C_i=\{x\}\cup P_i\), every useful exterior
partner \(\{x,y\}\) activates all \(t\) occurrences. Curvature is
concentrated precisely in the expensive charts.

### Corollary 2.3 (the exact abstract dichotomy)

Let

\[
N_\cap=\#\{i<j:C_i\cap C_j\ne\varnothing\},\qquad
N_\perp=\binom t2-N_\cap.
\tag{2.12}
\]

The enlarged all-pair common-partner catalog sees exactly the
\(N_\cap\) pairs and is blind to exactly the \(N_\perp\) pairs. Hence one
of these two sectors has size at least \(\frac12\binom t2\).

Put

\[
s=\left\lfloor\frac{m+q}{q+1}\right\rfloor.
\tag{2.13}
\]

No \(s+1\) collars can be pairwise disjoint. Turán's theorem applied to
the collar-disjointness graph gives

\[
N_\cap\ge
\left[\frac{t(t-s)}{2s}\right]_+.
\tag{2.14}
\]

In particular, when \(t\le s\), all collars may be disjoint and no
positive common-partner fraction follows from set size alone. The
overlapping-partner spike sector is genuinely necessary.

## 3. A fully legal owner-fixed spike

The next theorem repairs the fixed-factor defect of the earlier
coordinate-orbit spike construction. It also extends the owner-fixed
construction to \(q=1\).

### Theorem 3.1 (common-exterior owner-fixed spike)

Assume the setup of Section 1. Choose

\[
d_0\in Q_A\setminus U,
\tag{3.1}
\]

which is possible because \(q\le m-2\). For every coordinate

\[
c\in\bigcup_{i=1}^tD_i,
\]

freeze

\[
B_c=\{c,d_0\},\qquad
\theta_c=(c\,a)(d_0\,b),\qquad
F_{B_c}=\theta_cF_A.
\tag{3.2}
\]

For each occurrence choose one \(c_i\in D_i\), and let \(e_i'\) be the
corresponding token in the row \(\theta_{c_i}\pi_i\) of
\(F_{B_{c_i}}\).

Then:

1. \(e_i'\) has exactly the same lower endpoint and middle owner as
   \(e_i\), and every lower flag is fixed.
2. Arbitrary simultaneous old/alternate choices preserve the entire
   central matching, with zero released lower roots and zero changed
   middle owners.
3. At the distinguished depth,
   \[
   U_q(e_i')=(U\setminus\{c_i\})\cup\{a\}.
   \tag{3.3}
   \]
4. For arbitrary nonnegative upper weights, if \(z_i\) is the stacked
   old-to-alternate flag innovation, then
   \[
   \langle z_i,z_j\rangle_w\ge w_q
   \qquad(i\ne j).
   \tag{3.4}
   \]
   Consequently
   \[
   \boxed{
   \left\|\sum_i z_i\right\|_w^2-\sum_i\|z_i\|_w^2
   \ge 2w_q\binom t2.}
   \tag{3.5}
   \]
5. The \(c_i\)'s may be chosen so that the number of collision pairs
   among the new depth-\(q\) targets is at most
   \[
   \sum_{i<j}\frac{|D_i\cap D_j|}{q^2}
   \le\frac1q\binom t2.
   \tag{3.6}
   \]
   Hence a literal corner burns at least
   \[
   \left(1-\frac1q\right)\binom t2
   \tag{3.7}
   \]
   internal spike pairs for \(q\ge2\). At \(q=1\), it burns every pair.
6. If \(J_0\) is the old source-row run count, the conservative literal
   ledger for any binary old/alternate corner is
   \[
   J\le J_0+2t.
   \tag{3.7a}
   \]

#### Proof

Both \(c_i\) and \(d_0\) lie outside \(Y_i\): the first lies in the
right-suffix collar \(D_i\), and the second lies outside \(U\supset Y_i\).
Thus

\[
\theta_{c_i}S_i=S_i,\qquad
\theta_{c_i}Y_i=Y_i.
\tag{3.8}
\]

Every lower flag is a subset of \(S_i\), so it is also fixed. Since the
central edge \((S_i,Y_i)\) is fixed pointwise, replacing any collection
of tokens changes no lower owner and no middle owner. This proves the
first two assertions.

At depth \(q\), the old target contains \(c_i\), omits \(d_0\), and
avoids \(A\). Therefore (3.3) follows from (3.2).

At any upper depth \(p\), either the old target contains neither
\(c_i\) nor \(d_0\), in which case the innovation is zero, or its image
under \(\theta_{c_i}\) meets \(A\). Every old upper target avoids \(A\).
Hence for two nonzero innovations the two negative old/new cross
equalities are impossible, and

\[
\langle (z_i)_p,(z_j)_p\rangle
=\mathbf1_{\{U_p(e_i)=U_p(e_j)\}}
+ \mathbf1_{\{U_p(e_i')=U_p(e_j')\}}
\ge0.
\tag{3.9}
\]

At \(p=q\), the first indicator is one. Summing over depths proves
(3.4), and summing over \(i<j\) proves (3.5).

Finally choose each \(c_i\) independently and uniformly from \(D_i\).
By (3.3), the two new targets for \(i,j\) are equal exactly when
\(c_i=c_j\). Thus their collision probability is

\[
\frac{|D_i\cap D_j|}{q^2}\le\frac1q.
\]

Expectation and the probabilistic method give (3.6). At \(q=1\), the
sets \(D_i\) are singleton suffix coordinates. Lemma 4.1 below shows that
they are distinct for distinct occurrences of a common \(U\), so the new
targets are pairwise distinct.

Deleting one selected token can increase the old-row run count by at most
one, and inserting its alternate can create at most one destination-row
run. Summing over the tokens gives (3.7a). \(\square\)

### Legality scope

The theorem uses one fixed \(\theta_c\) and one fixed exact factor
\(F_{B_c}\) for each repeated partner \(B_c\). It does not use a separate
labelled copy of a factor for each occurrence. If two occurrences select
the same \(c\), their alternate rows are two rows of the same exact factor
\(F_{B_c}\).

The quantifier is a joint star choice from one source factor \(F_A\).
The theorem is not valid for already arbitrary factors \(F_B\), and it
does not simultaneously synchronize overlapping stars based at several
different source phases.

The theorem burns internal pairs of the old \(U\)-spike. It does not say
that the new targets avoid every target outside the spike.

## 4. The literal depth-one counterexample

### Lemma 4.1 (depth-one collars are pairwise disjoint)

For \(q=1\), distinct occurrences of one common \(U\) in one exact factor
have pairwise disjoint two-point collars.

#### Proof

For an occurrence with collar \(C_i=\{r_i,s_i\}\), the two sets

\[
U\setminus\{r_i\},\qquad U\setminus\{s_i\}
\tag{4.1}
\]

are exactly its two adjacent middle \(m\)-windows. If two collars shared
\(c\), then \(U\setminus\{c\}\) would be a middle window at both
occurrences. Exactness of \(F_A\) forces these to be the same physical
middle window.

A proper middle window in a cyclic row has two adjacent
\((m+1)\)-extensions, obtained by adjoining its left or right neighboring
coordinate. Those neighbors are distinct. Therefore the two extensions
cannot both equal \(U\). The two alleged occurrences must be the same
side extension and hence the same token, contrary to distinctness.
\(\square\)

The same argument also shows that a proper \(U_q\) occurs at most once in
one physical source row: a nonempty proper cyclic interval has a unique
start in a cyclic order of distinct coordinates.

### Lemma 4.2 (a repeated first-upper target always exists)

Every exact \(F_A\) contains a depth-one target of multiplicity at least
two.

#### Proof

There are

\[
A_m=\binom{2m-1}{m-1}
\]

phase-\(A\) starts, but only

\[
B_1=\binom{2m-1}{m+1}
\]

possible first-upper targets. Moreover

\[
A_m-B_1=\frac{W}{2m+1}>0.
\tag{4.2}
\]

Pigeonhole gives the claim. \(\square\)

Fix such a repeated target, with actual multiplicity \(t\ge2\). By
Lemma 4.1 write its disjoint collars as

\[
C_i=\{u_i,v_i\},\qquad 1\le i\le t.
\tag{4.3}
\]

Take \(A\) as the first-priority omitted pair. Complete it to the fixed
extraction partition as follows. Pair

\[
u_i\quad\text{with}\quad v_{i+1}
\tag{4.4}
\]

cyclically in \(i\), pair the remaining coordinates of \(Q_A\)
arbitrarily, and leave one coordinate unpaired.

### Theorem 4.3 (sharp failure of \(O(tq/m)\))

For the fixed partition (4.4):

1. no fixed partition partner is lower-active for any one of the \(t\)
   occurrences;
2. no arbitrary partner pair is lower-active for two different
   occurrences;
3. in the targetwise common-partner/overlapping-partner conjugate chart
   architecture, before any auxiliary cross-\(U\) repacketization,
   \[
   R_{\rm rel}
   +\#\{\text{newly used destination-factor rows}\}\ge r.
   \tag{4.4a}
   \]
   Here \(R_{\rm rel}\) counts unsaturated lower roots, equivalently
   deleted central token edges; if an alternate owner displaces a
   background token, that background token's lower root is counted.

If the operation charges a fraction \(\delta\) of the original
\(\binom t2\) collision pairs by removing pairs incident to moved
occurrences, then

\[
\binom t2-\binom{t-r}{2}\ge\delta\binom t2,
\tag{4.5}
\]

and therefore

\[
r\ge\frac{\delta(t-1)}2.
\tag{4.6}
\]

If instead the charge consists only of joined pair terms internal to the
\(r\) innovations, then

\[
\binom r2\ge\delta\binom t2,
\tag{4.7}
\]

which again forces \(r=\Omega_\delta(t)\).

Consequently, for every fixed \(K\) and \(\delta>0\), all sufficiently
large \(m\) violate

\[
\text{cost}\le K\frac{tq}{m}
\tag{4.8}
\]

at \(q=1\).

#### Proof

For occurrence \(i\), every fixed pair meeting \(C_i\) has its other
endpoint in a different collar \(C_j\subset U\setminus C_i=S_i\).
Every fixed pair meeting \(U\) outside \(C_i\) meets \(S_i\) directly.
Thus no fixed pair both avoids \(S_i\) and changes \(U\). Fixed pairs
wholly outside \(U\) may avoid \(S_i\), but they fix \(U\) and charge
nothing.

For two occurrences, Lemma 2.1 says that a common active partner would
require a nonempty subset of

\[
C_i\cap C_j,
\]

which is empty by Lemma 4.1. Hence every active external partner is
occurrence-specific and is not one of the fixed partition pairs.

The phase-one base extraction uses only the fixed partition factors.
Thus an alternate placed in an active external factor is a selected token
in a factor empty in the base extraction. Different moved occurrences use
different omitted pairs, so these alternates lie in different factors.
They create \(r\) singleton destination runs. Deleting an occurrence
without a legal replacement leaves its lower root unsaturated; reserving a
middle owner by deleting a background edge likewise releases that
background edge's lower root. The old occurrences lie in
distinct fully selected phase-one rows; deleting one token from such a
cyclic row leaves one nonempty cyclic run and does not cancel a destination
run. This proves the cost lower bound.

At most

\[
\binom t2-\binom{t-r}{2}
=\frac{r(2t-r-1)}2
\le rt
\]

old collision pairs are incident to the moved occurrences. This gives
(4.6). Equation (4.7) is immediate under the second charge convention.
Since \(t-1\ge t/2\), (4.6) gives cost at least
\(\delta t/4\), whereas the right side of (4.8) is \(Kt/m\).
\(\square\)

This is a literal counterexample inside an actual exact factor. It is not
merely an abstract collar set system. Its scope is precisely the requested
common-partner and overlapping-partner chart architecture. A direct
cross-row OR word which abandons factor-row charts is not ruled out.
The quantifiers are: for every exact \(F_A\), there is a repeated \(U\)
and a completion of \(A\) to a fixed extraction partition with the stated
obstruction. The theorem does not assert that every partition fixed in
advance, or every specially coordinated global factor system, contains
this blocked spike.

## 5. General factor-integral chronology bounds

### Proposition 5.1 (one carrier per touched occurrence)

For \(1\le q\le m-2\), a proper depth-\(q\) target \(U\) occurs at most
once in one physical exact-factor row. Hence a factor-integral chart
touching \(r\) occurrences of one \(U\) meets \(r\) distinct old source
rows.

If spike blocks \(I_\gamma\) cover a fraction \(\delta\binom t2\) of
collision pairs, and each block has size at most \(s\), then

\[
\sum_\gamma\binom{|I_\gamma|}{2}
\ge\delta\binom t2
\tag{5.1}
\]

implies

\[
\boxed{
\sum_\gamma |I_\gamma|
\ge
\frac{\delta t(t-1)}
     {\min\{s,t\}-1}.}
\tag{5.2}
\]

For pairwise-disjoint \((q+1)\)-collars one may take

\[
s=\left\lfloor\frac{m+q}{q+1}\right\rfloor.
\tag{5.3}
\]

In particular the component incidence is always
\(\Omega_\delta(t)\); when \(t>s\), (5.2) strengthens to order
\(\delta t^2q/m\).

#### Proof

Uniqueness of a proper cyclic interval proves the first assertion. For
\(k\le\min\{s,t\}\),

\[
\binom k2\le\frac{\min\{s,t\}-1}{2}\,k.
\]

Sum this inequality over the blocks and use (5.1). \(\square\)

Thus the earlier \(m/q\) curvature-per-boundary ratio is not a
constant-fraction pair-cover ledger. Formula (5.2) is a
component-incidence lower bound. It is not by itself a physical boundary
lower bound if several blocks share occurrence carriers or are fused in a
multiway cross-target row.

### Proposition 5.2 (common-row filler transfer)

Suppose \(t\) disjoint \((q+1)\)-collars are placed as disjoint cyclic
intervals in a proposed direct common-\(U\) row. Their marked token starts
have cyclic gaps at least \(q+1\). If a selected packet containing all
\(t\) marked starts has \(b\) selected runs and imports \(f\) additional
filler starts, then

\[
\boxed{f\ge q(t-b).}
\tag{5.4}
\]

#### Proof

Joining \(t\) marked starts into \(b\) runs bridges at least \(t-b\) of
the cyclic gaps between successive marked starts. Every bridged gap
contains at least \(q\) unmarked starts, all of which must be selected as
fillers. \(\square\)

If \(q=o(m)\), then \(b=O(tq/m)=o(t)\) forces the lower bound

\[
f\ge(1-o(1))tq.
\]

For a maximal disjoint spike \(t\asymp m/q\), this is order \(m\)
imported owners. A direct common-row recoding does not erase the ledger;
it transfers it to a global filler-extraction and seam problem.

## 6. Exact global accounting

### 6.1 The first-upper ledger

For phase one let

\[
\mu_1(U)=\#\{e:U_1(e)=U\}.
\]

Its duplicate-occurrence loss is

\[
\begin{aligned}
C_1(F_A)
&=\sum_U(\mu_1(U)-1)_+\\
&=A_m-|\operatorname {supp}\mu_1|\\
&=\frac{W}{2m+1}+h_1(F_A),
\end{aligned}
\tag{6.1}
\]

where

\[
h_1(F_A)
=\binom{2m-1}{m+1}
 -|\operatorname {supp}\mu_1|.
\tag{6.2}
\]

The arithmetic term \(W/(2m+1)\) is \(o(W/H)\) whenever \(H=o(m)\).
Thus the depth-one counterexample does not by itself disprove constant
one. It proves that collars cannot establish the needed global bound:
every depth-one duplicate pair lies in the disjoint-collar sector, and an
independently paid spike repair is admissible only if

\[
h_1(F_A)=o(W/H).
\tag{6.3}
\]

This is exactly the still-unproved near-rainbow first-shadow estimate,
unless a new cross-\(U\) braid shares the external carriers.

### 6.2 Gaussian repeated mass

At depth \(q\), phase one still has \(A_m\) occurrences, while the number
of possible local upper targets is

\[
B_{m,q}=\binom{2m-1}{m+q}.
\tag{6.4}
\]

Let

\[
M_q=\sum_{U:\mu_q(U)\ge2}\mu_q(U)
\]

be repeated-occurrence mass. Singleton targets occupy at most
\(B_{m,q}\) cells, so

\[
\boxed{M_q\ge A_m-B_{m,q}.}
\tag{6.5}
\]

For \(q=\lfloor \lambda\sqrt m\rfloor\), with fixed \(\lambda>0\),

\[
\frac{B_{m,q}}{A_m}
=\prod_{j=1}^q\frac{m-j}{m+j}
\longrightarrow e^{-\lambda^2}.
\tag{6.6}
\]

Indeed, taking logarithms gives

\[
\sum_{j=1}^q
\left(\log(1-j/m)-\log(1+j/m)\right)
=-\frac{q(q+1)}m+o(1).
\]

Since

\[
\frac{A_m}{W}=\frac{m+1}{2(2m+1)},
\]

(6.5) yields

\[
M_q\ge
\left(1-e^{-\lambda^2}+o(1)\right)A_m
=\Theta_\lambda(W).
\tag{6.7}
\]

Now suppose each repeated target is repaired independently and a fraction
\(\delta\) of its old pairs is charged by moving \(r_U\) occurrences.
By (4.6),

\[
\sum_U r_U
\ge\frac\delta2\sum_U(\mu_q(U)-1)_+
\ge\frac\delta2(A_m-B_{m,q})
=\Theta_{\delta,\lambda}(W).
\tag{6.8}
\]

Thus independently paid factor-row spikes have order-\(W\) occurrence
incidence at one Gaussian depth.

Even if the false hoped-for rate \(tq/m\) were granted formally, summing
it over the repeated mass in (6.7) gives, for \(q\asymp H\asymp\sqrt m\),

\[
\frac qm M_q=\Theta(W/H),
\tag{6.9}
\]

not \(o(W/H)\). Summing over a fixed positive-width interval in
\(q/\sqrt m\), hence over \(\Theta(\sqrt m)\) integer depths, gives
\(\Theta(W)\). The terminal form of the same proposed \(tq/m\) ledger is
\(WH/m\), which is again \(W/H\) when \(H\asymp\sqrt m\). This is an
accounting statement about that proposed ledger, not a lower bound on an
unknown cross-depth braid.

For the larger Boolean target \(H=\sqrt m\,\omega(m)\), the same terminal
ledger has ratio

\[
\frac{WH/m}{W/H}=\frac{H^2}{m}=\omega(m)^2
\tag{6.9a}
\]

to the allowed scale, so it is worse than boundary order.

Equation (6.8) is an obstruction to independent targetwise payment, not
to a cross-\(U\) word in which many targets share the same physical
intervals.

### 6.3 The correction for one fixed partner

The preceding per-occurrence ledger must not be misread as a lower bound
for one coherent fixed-\(B\) interval chart in the fully selected
phase-\(A\) rows. In one row, starts for which
a coordinate of \(B\) lies in the \(H\)-successor tail form one cyclic
interval per coordinate. For one chosen tail coordinate, owner-inertness
also asks that the other coordinate avoid the middle \(m\)-window. This
intersects the tail arc of length \(H\) with a complementary arc of length
\(m-1\). Their lengths sum to less than \(2m-1\), so the intersection is
one cyclic interval. Hence the two choices give at most two cyclic
intervals per \(F_A\) row. The old and alternate sides together use at
most

\[
4R_m
\tag{6.10}
\]

row intervals. Since

\[
\frac{R_m}{W}
=\frac{m+1}{2(2m-1)(2m+1)}
=\Theta(1/m),
\tag{6.11}
\]

one fixed-\(B\) all-depth tail chart is safely \(o(W/H)\) for \(H=o(m)\).

The obstruction is the renewal over many different partners. The exact
owner-inert activation fraction is

\[
\rho_q^0
=\frac{q(2m-q-3)}
       {2(2m-1)(m-1)}
=\left(1+O(q/m)\right)\frac q{2m}.
\tag{6.12}
\]

This is a menu average only. Disjoint collars receive zero common-partner
curvature for every \(B\), while concentrated intersection patterns put
all useful curvature in a few full-cost charts. No existing theorem
chooses and recenters a sufficient multi-\(B\) family while sharing the
\(O(R_m)\) row intervals.

### 6.4 A fixed-background full-star capacity obstruction

There is also no single background, fixed across the full arbitrary
old/alternate star menu, supporting every coherent owner-changing partner
chart.

For each of the \(A_m\) phase-\(A\) roots \(S\), let its old owner be

\[
Y(S)=S\cup\{p(S)\}.
\]

Freeze one orientation for every partner pair globally. Choose a partner
\(B(S)\) containing \(p(S)\) and a second point outside \(Y(S)\), and let
\(\alpha_S\in A\) be the frozen image of \(p(S)\). The alternate owner is

\[
Z(S)=S\cup\{\alpha_S\},\qquad \alpha_S\in A.
\tag{6.13}
\]

The \(A_m\) old owners \(Y(S)\) are distinct and avoid \(A\). The
\(A_m\) alternate owners \(Z(S)\) are distinct and meet \(A\). Thus the
two families are disjoint.

A fixed background has \(T-A_m\) other central roots. To leave all
\(Z(S)\)'s free for all coherent star endpoints, these background roots
must inject into only \(W-2A_m\) remaining middle owners. Indeed, a
background root owning \(Z(S)\) lies outside phase \(A\), because
\(Z(S)\) meets \(A\); under the stipulated unchanged-background
\(B(S)\)-endpoint it remains at \(Z(S)\) and collides with the switched
root \(S\). Necessarily

\[
T-A_m\le W-2A_m,
\]

or

\[
A_m\le W-T.
\tag{6.14}
\]

But

\[
T+A_m-W
=W\frac{m^2-5m-2}{2(2m+1)(m+2)}
=\left(\frac14+o(1)\right)W,
\tag{6.15}
\]

which is positive for \(m\ge6\). Restoring a universal fixed-background
full-star menu by releasing background lower roots or deleting their
central tokens therefore costs at least the quantity in (6.15).

This capacity obstruction concerns owner-changing full coherent charts.
The owner-inert tail spike of Theorem 3.1 avoids it. What remains for that
tail spike is multi-\(B\) chronology and energy orientation.

### 6.5 Positive Gram is not current-state descent

Suppose \(a\) labelled occurrences are moved from a target of current load
\(X\) to one target of current load \(Y\), using fair independent bits.
If \(K\sim\operatorname {Bin}(a,1/2)\), the exact expected change of the
pair-collision polynomial is

\[
\begin{aligned}
\mathbb E\bigg[
\binom{X-K}{2}+\binom{Y+K}{2}
-\binom X2-\binom Y2
\bigg]
&=\mathbb E\,[K(Y-X)+K^2]\\
&=\frac a4\bigl(2(Y-X)+a+1\bigr).
\end{aligned}
\tag{6.16}
\]

Descent requires

\[
X-Y>\frac{a+1}{2}.
\tag{6.17}
\]

The ordinary adjacent-integer floor correction cancels in this two-cell
calculation because the two targets have the same rank and their combined
load is fixed. Thus the positive cross-Gram term charges spike curvature relative to the
two coherent endpoints, but freezing the rest of a full coherent
\(B\)-chart may leave adverse linear drift. A literal constant-one
argument still needs either a pair-symmetric endpoint with controlled
energy or an independent load-oriented target-flow/recentering lemma.

## 7. Independently audited boundary

The decisive legality and chronology steps were audited independently.
The following points survived both audits.

1. One permutation and one exact factor must be frozen per repeated
   omitted pair. Theorem 3.1 does this; occurrencewise orientations are
   not used.
2. Collar intersection is sufficient only for the enlarged all-pair
   containment catalog. A frozen partition additionally needs an
   available compatible factor and a legal common background.
3. Theorem 3.1 preserves the actual central edges pointwise. Its zero
   release count is therefore literal, not an abstract matching
   completion.
4. A proper common \(U_q\) occurs in distinct physical rows, and at
   \(q=1\) exactness forces the collars to be pairwise disjoint.
5. The cyclic cross-pairing (4.4) eliminates every active fixed partner
   while leaving a genuine exact phase-one factor. Hence the linear
   singleton-run lower bound is physical for the independently paid
   one-\(U\) architecture.
6. The internal pair burn and joined Gram do not imply global floor-energy
   descent; (6.16) is the missing orientation term.

The exact proved/conditional boundary is therefore:

- **proved:** the common-partner incidence formulas (2.5)--(2.10);
- **proved:** a legal zero-owner-release spike charging all joined pairs
  and literally burning at least half the internal spike at every depth;
- **proved:** the targetwise, independently paid one-\(U\)
  \(O(tq/m)\) chronology is false, sharply already at \(q=1\);
- **proved:** independent targetwise aggregation reaches at least the
  Gaussian boundary scale and cannot compose quantitatively into
  constant one;
- **proved:** a universal unchanged-background full-star menu has a
  \(\Theta(W)\) owner-capacity deficit;
- **unproved:** a cross-\(U\), multi-\(B\), cross-row literal braid with
  total carrier loss \(o(W/H)\);
- **unproved:** a common-endpoint or load-oriented recentering theorem
  turning the legal spike curvature into descent from the current
  coefficient-one floor profile.

No labelled synchronization theorem, MWB theorem, or sharp contiguous-OR
constant follows from the proved statements.
