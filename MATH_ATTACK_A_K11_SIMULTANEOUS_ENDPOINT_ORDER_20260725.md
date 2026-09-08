# Next A wave: simultaneous endpoint order at \(k=11\)

Date: 2026-07-25

## 0. Verdict

Assume the audited length-\(465\), zero-margin \(k=11\) normal form.  This
attack does **not** derive a contradiction, so

\[
465\leq\nu(11)\leq477
\]

remains the certified interval.

This report proves two new order-sensitive forbidden cuts and one
independently verified quotient construction.

1. Four neighboring rank-seven hull complements constrain one physical
   rank-four pair color.  Since the regular physical pair colors are
   distinct, these local candidate families obey an exact Hall system.
   In particular, two regular sites cannot have the same seven-point
   hull-complement union.

2. In the odd-\(E\) five-facet parity branch from the preceding A wave,
   let

   \[
   \mathcal O=\binom B4
   \]

   be the five even-\(V_Y\) colors.  At most \(15\) regular rank-four
   sites can see two distinct colors of \(\mathcal O\) in their ordered
   hull neighborhood.  Sixteen such sites are impossible.

3. A complementary run cut charges every separated return of the
   \(X\)-containing rank-seven hulls against the forced rank-four support:

   \[
   \boxed{
   \kappa_X+r_X
   \leq
   \sum_{Y\cap X=\varnothing}c_Y+u_X+\iota_X,
   \qquad u_X+\iota_X\leq2.}
   \]

4. Conversely, in the symmetric branch

   \[
   E=132,\qquad V_Y=5\quad\text{for every }Y,
   \]

   every simple path in the resulting \(4\)-\((11,5,2)\) design graph
   canonically lifts to an endpoint-ordered Johnson word fragment with
   the correct inclusion matching and explicit rank-four turns.  The lift
   is collision-free across a vertex-disjoint path cover.

Thus the new cuts eliminate nontrivial ordered hull classes, while the
quotient construction proves a barrier: endpoint order by itself cannot
exclude the \(E=132\) design branch.  A finishing proof must force a
Hall-deficient clustering, violate the separated-run cut, or use physical
rank-at-most-three entry geometry beyond the quotient.

No web lookup, solver, finite search, or computational enumeration is used.

## 1. Frozen central order

Let

\[
A_0,\ldots,A_{m-1}\subseteq\Omega=[11]
\]

be the central rank-at-most-three word.  Put

\[
B_i=A_i\cup A_{i+1},\qquad
C_i=A_i\cup A_{i+1}\cup A_{i+2},\qquad
T_i=A_i\cup\cdots\cup A_{i+3},
\tag{1.1}
\]

and let \(H=C_s\) be the seam triple.

The retained central edge sites are

\[
P_L=\{1,\ldots,s-1\},\qquad
P_R=\{s+2,\ldots,m-3\},\qquad
P=P_L\mathbin{\dot\cup}P_R,
\tag{1.2}
\]

with empty ranges understood.  A site \(p\in P\) indexes the retained edge
between \(C_{p-1}\) and \(C_p\).  Put

\[
K_p=C_{p-1}\cap C_p.
\tag{1.3}
\]

The endpoint-ordered matching gives the paired rank-seven hull

\[
R_p=
\begin{cases}
T_{p-1}\cup T_p
=\operatorname{OR}(A_{p-1},\ldots,A_{p+3}),
&p\in P_L,\\[2mm]
T_{p-2}\cup T_{p-1}
=\operatorname{OR}(A_{p-2},\ldots,A_{p+2}),
&p\in P_R,
\end{cases}
\tag{1.4}
\]

and its four-set complement

\[
Y_p=\Omega\setminus R_p.
\tag{1.5}
\]

Call \(p\) **regular** when \(|B_p|=4\).  Then

\[
K_p=B_p.
\tag{1.6}
\]

All sites are regular except possibly the unique internal extra-low-pair
site in mode C0.  At the regular sites, the \(K_p\) are distinct selected
rank-four target values.

If retained, the left and right interface hulls have complements
\(Y_L,Y_R\).  Their literal intervals are respectively

\[
[L-1,L+3],\qquad [R-3,R+1].
\tag{1.7}
\]

## 2. The ordered four-hull Hall cut

For a regular site \(p\), define

\[
N(p)=
\bigl(P_L\cap[p-2,p+1]\bigr)
\cup
\bigl(P_R\cap[p-1,p+2]\bigr).
\tag{2.1}
\]

The two ranges differ because the right central path is oppositely
oriented.  Put

\[
\begin{aligned}
\mathcal I(p)
={}&
\{Y_L:\text{the left interface is retained and }p\in\{1,2\}\}\\
&{}\cup
\{Y_R:\text{the right interface is retained and }
p\in\{m-4,m-3\}\},
\end{aligned}
\tag{2.2}
\]

and

\[
U_p=
\left(\bigcup_{q\in N(p)}Y_q\right)
\cup
\left(\bigcup_{Y\in\mathcal I(p)}Y\right).
\tag{2.3}
\]

### Theorem 2.1 (ordered disjointness)

For every regular \(p\in P\),

\[
\boxed{K_p\cap U_p=\varnothing.}
\tag{2.4}
\]

Consequently

\[
\boxed{
|U_p|\leq7,\qquad
K_p\in\binom{\Omega\setminus U_p}{4}.}
\tag{2.5}
\]

#### Proof

For \(q\in P_L\), the literal hull interval of \(R_q\) is

\[
[q-1,q+3].
\]

It contains both entries \(A_p,A_{p+1}\) exactly when

\[
p-2\leq q\leq p+1.
\]

Thus every \(q\in P_L\cap[p-2,p+1]\) has

\[
K_p=B_p\subseteq R_q,
\]

and hence \(K_p\cap Y_q=\varnothing\).

For \(q\in P_R\), the hull interval is

\[
[q-2,q+2].
\]

It contains \(A_p,A_{p+1}\) exactly when

\[
p-1\leq q\leq p+2.
\]

This proves disjointness from every central complement in (2.1).

The left interface hull contains \(A_0,\ldots,A_3\), and therefore
contains \(B_1,B_2\).  The reversed right interface contains
\(B_{m-4},B_{m-3}\).  This proves disjointness from the applicable
interface complements.  Equation (2.4) follows.  Since \(|K_p|=4\) on an
eleven-point ground set, (2.5) follows.  \(\square\)

Let

\[
\mathscr S\subseteq\binom{\Omega}{4}
\]

be any proposed physical rank-four support containing every regular
\(K_p\), and define

\[
\mathcal A_p(\mathscr S)
=
\mathscr S\cap\binom{\Omega\setminus U_p}{4}.
\tag{2.6}
\]

### Theorem 2.2 (exact rank-four SDR criterion)

For every \(J\subseteq P_{\rm reg}\),

\[
\boxed{
\left|
\bigcup_{p\in J}\mathcal A_p(\mathscr S)
\right|
\geq |J|.}
\tag{2.7}
\]

Conversely, the cuts (2.7) are sufficient for assigning distinct abstract
rank-four labels from \(\mathscr S\) to the regular sites subject only to
the ordered disjointness (2.4).  They are exact for this quotient
assignment, though not sufficient for a physical word.

#### Proof

The actual map \(p\mapsto K_p\) is a system of distinct representatives
for the families \(\mathcal A_p(\mathscr S)\).  This proves necessity.
Sufficiency is Hall's marriage theorem.  \(\square\)

### Corollary 2.3 (explicit forbidden classes)

If \(|U_p|=7\), then

\[
K_p=\Omega\setminus U_p.
\]

Therefore

\[
\boxed{
p\ne r,\quad |U_p|=|U_r|=7,\quad U_p=U_r
\quad\Longrightarrow\quad\text{impossible}}
\tag{2.8}
\]

for regular sites.

More generally, if \(Z\subseteq U_p\) for every regular \(p\in J\), then

\[
\boxed{
|J|
\leq
\left|
\mathscr S\cap\binom{\Omega\setminus Z}{4}
\right|
\leq
\binom{11-|Z|}{4}.}
\tag{2.9}
\]

#### Proof

The first assertion is the singleton case of (2.5).  In the second,
every candidate family in (2.7) lies in
\(\mathscr S\cap\binom{\Omega\setminus Z}{4}\).  \(\square\)

The local inequality \(|U_p|\leq7\) alone is only a physical-overlap
observation.  The simultaneous SDR cut (2.7), using exact rank-four target
ownership, is the new content.

## 3. The C0 defect

Suppose the extra low pair is internal to a central forest edge at the
unique exceptional site \(p_*\).  Its intersection color

\[
K_{p_*}=C_{p_*-1}\cap C_{p_*}
\]

is still a four-set, but need not equal \(B_{p_*}\).  The multi-hull
containment from Theorem 2.1 need not hold.  Complement duality still gives

\[
K_{p_*}\cap Y_{p_*}=\varnothing.
\tag{3.1}
\]

Define

\[
V_p=
\begin{cases}
U_p,&p\ne p_*,\\
Y_{p_*},&p=p_*,
\end{cases}
\qquad
\mathcal A_p=
\mathscr S_c\cap\binom{\Omega\setminus V_p}{4},
\tag{3.2}
\]

where

\[
\mathscr S_c=\{K_p:p\in P\}
\]

is the actual central intersection support.

The exceptional color can collide with at most one regular selected color,
and there are no other collisions.  Hence, for every \(J\subseteq P\),

\[
\boxed{
\left|\bigcup_{p\in J}\mathcal A_p\right|
\geq
|J|-\mathbf1_{\{p_*\in J\}}.}
\tag{3.3}
\]

For \(J\subseteq P\setminus\{p_*\}\), the exact Hall bound (2.7) remains
valid.

## 4. Coupling the parity shadow to endpoint order

Assume \(E\) is odd and the small parity alternative from the preceding A
wave occurs.  Then there is a unique five-set \(B\) such that

\[
\mathcal O
=
\{Y:V_Y\text{ is even}\}
=
\binom B4.
\tag{4.1}
\]

Let \(J_B\) consist of the regular sites \(p\) whose ordered hull
neighborhood from (2.1)--(2.3) contains two distinct colors from
\(\mathcal O\).

### Theorem 4.1 (the fifteen-site parity cut)

\[
\boxed{
|J_B|
\leq
\left|
\mathscr S\cap\binom{\Omega\setminus B}{4}
\right|
\leq15.}
\tag{4.2}
\]

Thus an odd-\(E\) candidate in the five-facet parity branch with sixteen
such regular sites is impossible.

#### Proof

Two distinct four-facets of \(B\) have union \(B\).  Therefore

\[
B\subseteq U_p
\qquad(p\in J_B).
\]

Apply (2.9) with \(Z=B\):

\[
|J_B|
\leq
\left|
\mathscr S\cap\binom{\Omega\setminus B}{4}
\right|
\leq
\binom64=15.
\]

\(\square\)

This is a direct coupling of the simultaneous \(330\)-color parity shadow,
the endpoint order, and literal rank-four ownership.  It is not implied by
the earlier scalar or coordinatewise ledgers.  The theorem does not assert
that \(|J_B|\geq16\); forcing that clustering is a remaining problem.

## 5. A separated-run forbidden cut

The four-hull cut has a useful two-hull projection that counts separated
returns exactly.

Write the nonempty postcut central six-set pieces as

\[
W^a_0,W^a_1,\ldots,W^a_{\ell_a},
\qquad 1\leq a\leq b_H.
\tag{5.1}
\]

Their central hulls are

\[
Q^a_i=W^a_{i-1}\cup W^a_i,\qquad
Y^a_i=\Omega\setminus Q^a_i,
\qquad1\leq i\leq\ell_a.
\tag{5.2}
\]

Let \(K^a_i\) be the attached rank-four lower intersection color.  If
piece \(a\) has a retained interface hull \(Q^a_0\), put

\[
M^a_1=Q^a_0\cap Q^a_1;
\]

otherwise put \(M^a_1=Q^a_1\).  For \(i\geq2\), put

\[
M^a_i=Q^a_{i-1}\cap Q^a_i.
\tag{5.3}
\]

### Lemma 5.1 (two-hull carrier)

\[
\boxed{K^a_i\subseteq M^a_i.}
\tag{5.4}
\]

At a genuine predecessor,

\[
M^a_i=\Omega\setminus(Y^a_{i-1}\cup Y^a_i).
\tag{5.5}
\]

Thus \(|M^a_i|=6\) at a nonlazy transition and \(7\) at a lazy transition
or an unentered start.

#### Proof

Write the corresponding oriented five-set path as

\[
S_0\to S_1\to\cdots,\qquad \Phi(S_j)=W^a_j.
\]

The hull \(Q_i\) is attached to \(S_{i-1}\to S_i\), with lower color

\[
K_i=S_{i-1}\cap S_i.
\]

For \(i\geq2\),

\[
K_i\subseteq S_{i-1}\subseteq W^a_{i-1}
\subseteq Q_{i-1}\cap Q_i.
\]

At an entered first position, the same argument uses the actual external
predecessor hull.  At an unentered start, \(K_1\subseteq Q_1\).  This proves
(5.4); equation (5.5) is complementation.  \(\square\)

Fix \(X\subseteq\Omega\), \(|X|\leq4\), and define

\[
g_X
=
\#\{(a,i):X\subseteq Q^a_i\}
=
\sum_{\substack{Y\in\binom{\Omega}{4}\\Y\cap X=\varnothing}}c_Y.
\tag{5.6}
\]

Let \(r_X\) be the total number of maximal runs of \(X\)-containing
central hulls, counted separately in the postcut pieces.  Let

* \(u_X\) count unentered pieces whose first central hull contains \(X\);
* \(\iota_X\) count retained interfaces for which both the interface hull
  and the first central hull contain \(X\).

A piece with \(\ell_a=0\) has no central hull and contributes zero to
\(r_X,u_X,\iota_X\).

Then

\[
u_X+\iota_X\leq b_H\leq2.
\tag{5.7}
\]

Let \(\kappa_X\) be the number of actual central lower-color occurrences
containing \(X\).

### Theorem 5.2 (separated-run cut)

\[
\boxed{
\kappa_X+r_X
\leq
\sum_{Y\cap X=\varnothing}c_Y+u_X+\iota_X.}
\tag{5.8}
\]

#### Proof

A run of \(s\) consecutive \(X\)-containing hulls supplies \(s-1\)
positions whose two neighboring hulls both contain \(X\).  Its first
position supplies one additional capable carrier exactly when it is an
unentered start counted by \(u_X\), or its retained interface predecessor
also contains \(X\), counted by \(\iota_X\).  Therefore the number of
positions whose carrier \(M^a_i\) contains \(X\) is exactly

\[
g_X-r_X+u_X+\iota_X.
\]

Every position whose actual lower color contains \(X\) is among these
capable positions by Lemma 5.1.  Rearrangement gives (5.8).  \(\square\)

This is strictly stronger than the edgewise condition
\(K_i\cap Y_i=\varnothing\): every separated return costs one additional
rank-four slot, except at at most two genuine starts or interfaces.

### Corollary 5.3 (physical rank-four forms)

At \(n_5=133\), let

* \(\lambda_X\) count literal rank-four boundary values containing \(X\);
* \(h_X=\mathbf1_{\{X\subseteq H\}}\);
* \(\varepsilon_X\) count endpoint-excluded selected rank-four pair colors
  containing \(X\).

The exact rank-four partition gives

\[
\kappa_X=
\binom{11-|X|}{4-|X|}
-\lambda_X-h_X-\varepsilon_X.
\]

Hence

\[
\boxed{
\binom{11-|X|}{4-|X|}
-\lambda_X-h_X-\varepsilon_X+r_X
\leq
\sum_{Y\cap X=\varnothing}c_Y+u_X+\iota_X.}
\tag{5.9}
\]

For an \(n_5=132\) mode, let

\[
\delta_4=\mathbf1_{\{|H|=4\}},
\]

use the analogous distinct literal and endpoint-excluded counts
\(\lambda_X,\varepsilon_X\), and in C0 put \(\xi=1\) when the extra low
pair is internal, with rank-four intersection \(K_*\).  The
collision-safe occurrence bound is

\[
\kappa_X\geq
\binom{11-|X|}{4-|X|}
-\lambda_X-\delta_4h_X-\varepsilon_X
+\xi\mathbf1_{\{X\subseteq K_*\}}.
\]

Therefore

\[
\boxed{
\begin{aligned}
&\binom{11-|X|}{4-|X|}
-\lambda_X-\delta_4h_X-\varepsilon_X
+\xi\mathbf1_{\{X\subseteq K_*\}}+r_X\\
&\hspace{24mm}\leq
\sum_{Y\cap X=\varnothing}c_Y+u_X+\iota_X.
\end{aligned}}
\tag{5.10}
\]

The plus sign on the C0 term is essential: \(\kappa_X\) counts
occurrences, so the exceptional edge contributes even if \(K_*\) repeats
an ordinary color.

## 6. Canonical quotient in the \(E=132\) design branch

Assume

\[
E=132,\qquad V_Y=5\quad\text{for all }Y.
\tag{6.1}
\]

The external complementary five-set family \(\mathcal H\) is a simple
\(4\)-\((11,5,2)\) design.  Put

\[
G=J(11,5)[\mathcal H].
\]

For \(B\in\mathcal H\), let \(B^\perp\) be its unique disjoint design
block.  For an edge \(BB'\) of \(G\), put

\[
\lambda(BB')=\Omega\setminus(B\cup B').
\tag{6.2}
\]

The preceding A wave proved that this edge-label map is a bijection from
\(E(G)\) to

\[
\binom{\Omega}{5}\setminus\mathcal H.
\tag{6.3}
\]

At a fixed block \(B\), the five incident labels are exactly the five
five-subsets of

\[
C_B=\Omega\setminus B
\]

other than \(B^\perp\).  Indeed, all incident labels are distinct
five-subsets of \(C_B\) outside \(\mathcal H\), while \(B^\perp\) is the
unique member of \(\mathcal H\) among the six five-subsets of \(C_B\).

### Theorem 6.1 (canonical path lift)

Let

\[
B_0,B_1,\ldots,B_\ell
\]

be a simple path in \(G\).  Define

\[
S_0=B_0^\perp,\qquad
S_i=\lambda(B_{i-1}B_i)
\quad(1\leq i\leq\ell),
\tag{6.4}
\]

and

\[
U_i=\Omega\setminus B_i.
\tag{6.5}
\]

Then the \(S_i\) are distinct five-sets, the \(U_i\) are distinct
six-sets, and

\[
\boxed{
S_i\cap S_{i+1}\in\binom{\Omega}{4},\qquad
S_i\cup S_{i+1}=U_i
\quad(0\leq i<\ell).}
\tag{6.6}
\]

Moreover,

\[
\Phi(S_i)=U_i
\quad(0\leq i\leq\ell)
\tag{6.7}
\]

is an endpoint-ordered inclusion matching on the fragment.  The terminal
color \(U_\ell\) may be omitted at a component root or left open for an
inward interface.

The construction extends without source or union-color collisions to
every vertex-disjoint path cover of \(G\).

#### Proof

The start source \(S_0=B_0^\perp\) belongs to \(\mathcal H\); every later
\(S_i\) is an edge label outside \(\mathcal H\).  The edge labels are
globally injective, and disjoint partners are distinct, so the sources are
distinct within a path and across a vertex-disjoint path cover.  The
\(U_i\) are distinct because the \(B_i\) are.

At \(i=0\), the sets \(S_0,S_1\) are two distinct five-subsets of
\(U_0=\Omega\setminus B_0\).  For \(i\geq1\), the sources
\(S_i,S_{i+1}\) are the two distinct labels of consecutive design edges
incident with \(B_i\), hence again two distinct five-facets of \(U_i\).
Their intersection has size four and their union is \(U_i\), proving
(6.6).

Every \(S_i\) is disjoint from \(B_i\), so \(S_i\subset U_i\), and (6.7)
is an inclusion matching.  The alternating fragment is

\[
S_0,U_0,S_1,U_1,\ldots,S_\ell,U_\ell.
\]

The collision statements already proved make the componentwise extension
valid.  \(\square\)

### Rank-four turn audit

Write

\[
B^\perp=(\Omega\setminus B)\setminus\{g_B\}.
\]

Every incident label at \(B\) is

\[
(\Omega\setminus B)\setminus\{z\},
\qquad z\ne g_B.
\]

Thus the initial turn at \(B_0\) has intersection

\[
(\Omega\setminus B_0)\setminus\{g_{B_0},z\},
\]

while an internal turn at \(B\) has intersection

\[
(\Omega\setminus B)\setminus\{z,z'\},
\qquad z\ne z',\quad z,z'\ne g_B.
\tag{6.8}
\]

The initial rank-four turn omits \(g_B\); every internal turn contains
\(g_B\).  This verifies the lower-rank quotient explicitly.

Theorem 6.1 does not construct the central rank-at-most-three physical
entries, nor prove that a path cover exists with all central attachments.
It proves the narrower barrier: endpoint order and inclusion matching
alone do not forbid a design path.

## 7. Adversarial audit and remaining gate

1. **Right-side indexing.**  On \(P_R\), the matched six-sets are
   \(T_{p-1}\) and \(T_{p-2}\).  The hull interval begins at \(p-2\),
   producing the shifted neighborhood in (2.1).

2. **Seam.**  Sites \(p=s,s+1\) are absent.  Runs in Section 5 are counted
   separately in the postcut pieces.  No seam edge or artificial
   concatenation is used.

3. **Interfaces.**  An interface complement is included only when the
   physical interface is retained and its literal hull contains the
   relevant regular pair.  Interfaces shrink candidate families and
   cannot repair a failed Hall cut.

4. **C0.**  Multi-hull containment is used only at regular sites.  The
   exceptional intersection has only its paired-complement constraint and
   one possible collision, exactly as in (3.1)--(3.3) and (5.10).

5. **Hall scope.**  The converse in Theorem 2.2 concerns only assignment
   of distinct rank-four labels to the displayed candidate families.  It
   is not a word-realization theorem.

6. **Separated runs.**  The capable-position count

   \[
   g_X-r_X+u_X+\iota_X
   \]

   is exact.  Inequality enters only because a capable carrier need not
   actually contain \(X\).

7. **Design quotient.**  Starts lie in \(\mathcal H\), nonstart sources
   are distinct labels outside \(\mathcal H\), and union colors are indexed
   by distinct design vertices.  Thus the quotient has no hidden source
   or union collision.

8. **No full contradiction.**  The parity theorem does not force the five
   special colors to cluster, and the separated-run inequalities retain
   slack.  The design quotient does not impose the physical entry
   filtration.

The smallest remaining order lemma is now explicit:

> Every length-\(465\) survivor forces either a Hall-deficient family in
> (2.7), a violation of the separated-run cut (5.9) or (5.10), or an
> \(E=132\) design path cover whose canonical lift cannot be extended
> through the central rank-at-most-three filtration and at most two
> six-mode interfaces.

This trichotomy is unproved.  In the odd-\(E\) five-facet branch, it would
suffice to prove \(|J_B|\geq16\).
