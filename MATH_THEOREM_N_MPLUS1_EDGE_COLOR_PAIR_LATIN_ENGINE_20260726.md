# The \((m+1)\)-edge-coloring engine: local pair maps, exact defect averaging, and the Steiner-resolution barrier

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 {\cal L}=\binom{[2m]}{m-1},\qquad
 {\cal M}=\binom{[2m]}m,\qquad
 {\cal U}=\binom{[2m]}{m+1},
\]

\[
 W=|{\cal M}|,\qquad
 N=|{\cal L}|=|{\cal U}|={m\over m+1}W,\qquad
 C=W-N={W\over m+1}=\operatorname {Cat}_m.
 \tag{0.1}
\]

Let \(H_m\) be the bipartite inclusion graph between \({\cal L}\) and
\({\cal M}\). Its two degrees are \(m+1\) and \(m\), so König's theorem
gives a proper edge-coloring with a color set \({\mathscr C}\) of size

\[
 n=m+1.
 \tag{0.2}
\]

Fix such a coloring \(\kappa\). Every lower set sees all \(n\) colors,
while every middle set has one missing color \(\mu(X)\).

For each \(U\in{\cal U}\), the coloring induces an exact local pair map

\[
 \psi_U:\binom U2\longrightarrow\binom{\mathscr C}2.
 \tag{0.3}
\]

For a color pair \(p\), its fibre size

\[
 h_p(U)=|\psi_U^{-1}(p)|
 \tag{0.4}
\]

is precisely the multiplicity of upper color \(U\) in the Johnson
pseudofactor obtained from the two color classes in \(p\).

Let

\[
 Q=\binom n2=\binom{m+1}2.
 \tag{0.5}
\]

Both the domain and codomain of every \(\psi_U\) have size \(Q\). Define
the local Latin defect

\[
 \ell(U)=Q-|\operatorname {im}\psi_U|
        =|\{p:h_p(U)=0\}|
 \tag{0.6}
\]

and its total

\[
 {\mathfrak L}(\kappa)=\sum_{U\in{\cal U}}\ell(U).
 \tag{0.7}
\]

The exact averaging identity is

\[
 \boxed{\sum_{p\in\binom{\mathscr C}2}H_p
       ={\mathfrak L}(\kappa),}
 \qquad
 H_p:=|\{U:h_p(U)=0\}|.
 \tag{0.8}
\]

Consequently some pair satisfies

\[
 \boxed{
 H_p\le
 \left\lfloor{{\mathfrak L}(\kappa)\over Q}\right\rfloor.}
 \tag{0.9}
\]

For that pair, the upper collision excess equals \(H_p\), the lower
colors are still exact, and middle degree is at most two. Thus

\[
 {\mathfrak L}(\kappa)=o(QN)
 \tag{0.10}
\]

is a sharp sufficient average-local condition for one color pair with
\(o(W)\) missing upper colors. If
\({\mathfrak L}(\kappa)<Q\), one color pair is upper-perfect exactly.

Demanding every local map \(\psi_U\) to be a bijection is much stronger.
It forces the missing-color classes

\[
 {\cal E}_c=\{X\in{\cal M}:\mu(X)=c\}
 \tag{0.11}
\]

to partition \({\cal M}\) into \(m+1\) Steiner systems

\[
 S(m-1,m,2m).
 \tag{0.12}
\]

In fact, the complete Steiner divisibility conditions force

\[
 \boxed{m+1\text{ prime}}
 \tag{0.13}
\]

when \(m\ge2\). Hence the universal local-Latin target is impossible
whenever \(m+1\) is composite, including every odd \(m\ge3\). This does
not obstruct a single distinguished pair: (0.10) permits a vanishing
average fraction of local pair defects and does not require a Steiner
resolution.

Finally, the local missing-color permutation forced by a Steiner
resolution does not, by itself, force the local pair map to be Latin.
There is a legal four-vertex local table whose missing colors are all
distinct but whose pair map has two holes and two double fibres. Thus the
edge-coloring engine has two separate gates:

1. missing-color/Steiner resolution controls the one-color margins;
2. pair-map Latinness controls the genuine two-color unions.

## 1. Proper color classes and the exact endpoint design

For \(S\in{\cal L}\) and \(c\in{\mathscr C}\), let

\[
 f_c(S)
 \tag{1.1}
\]

be the unique middle extension of \(S\) whose incident edge has color
\(c\). It exists and is unique because \(S\) has degree \(n\) and sees
all \(n\) colors.

Every color class is a matching of size \(N\), saturating \({\cal L}\)
and using \(N\) distinct vertices of \({\cal M}\). Every middle vertex has
degree \(m=n-1\), so exactly one color is missing there.

### Lemma 1.1 (missing-color partition)

For every \(c\in{\mathscr C}\),

\[
 |{\cal E}_c|=W-N=C,
 \tag{1.2}
\]

and the \(n\) families \({\cal E}_c\) partition \({\cal M}\).

#### Proof

The color-\(c\) matching hits exactly \(N\) middle vertices, hence misses
\(W-N=C\). A middle vertex is missed by exactly its unique absent color.
\(\square\)

Fix two distinct colors \(\alpha,\beta\), and put
\(p=\{\alpha,\beta\}\). Their union in \(H_m\) has degree two at every
lower vertex. At a middle vertex \(X\), its degree is one if
\(\mu(X)\in p\), and two otherwise.

### Proposition 1.2 (exact two-color path ledger)

The \(\alpha,\beta\) subgraph has endpoint set

\[
 {\cal E}_\alpha\mathbin{\dot\cup}{\cal E}_\beta,
 \tag{1.3}
\]

of size \(2C\). It is a disjoint union of exactly \(C\) alternating paths
and an arbitrary number \(z_p\) of alternating cycles.

Suppressing every lower vertex gives a Johnson graph on all \(W\) middle
vertices with

1. one edge of every lower color \(S\in{\cal L}\);
2. middle degree one on (1.3) and degree two elsewhere; and
3. exactly \(C+z_p\) components.

#### Proof

The two color classes are matchings. Hence their union has maximum degree
two and its components are alternating paths and cycles. Exactly the
vertices missing \(\alpha\) or \(\beta\) have degree one; the two missing
families are disjoint by Lemma 1.1. Every path has two endpoints, so there
are \(C\) paths. Suppression at \(S\) joins the two distinct extensions
\(f_\alpha(S),f_\beta(S)\), which are Johnson adjacent with intersection
\(S\). \(\square\)

Thus this engine naturally produces the Catalan number of path components,
not a 2-factor. This is coefficient-safe at the component-count scale:
if \(H=o(m)\), then

\[
 C={W\over m+1}=o(W/H).
 \tag{1.4}
\]

The additional cycle count \(z_p\) remains uncontrolled.

This object must not be identified with the paired-SCD 2-factor. A paired
central factor has \(C\) isolated middle owners and degree two on the
other \(N\) owners. A bichromatic factor has no isolated middle owner and
has the \(2C\) degree-one endpoints in (1.3). Closing or reassigning those
endpoints is a separate integral matching problem. The advantage of the
present engine is instead that a path factor can be compiled directly if
its upper-color and cycle defects are controlled.

## 2. The local color-pair map

Fix \(U\in{\cal U}\). For \(a\in U\), put

\[
 X_a=U\setminus\{a\},
 \tag{2.1}
\]

and, for distinct \(a,b\in U\), put

\[
 S_{ab}=U\setminus\{a,b\}.
 \tag{2.2}
\]

Define the ordered half-edge color

\[
 \lambda_U(a,b)=\kappa(S_{ab},X_a).
 \tag{2.3}
\]

### Lemma 2.1 (local half-edge identities)

For every \(U\):

1. for fixed \(a\), the map
   \[
   b\longmapsto\lambda_U(a,b)
   \]
   is a bijection
   \[
   U\setminus\{a\}\longrightarrow
   {\mathscr C}\setminus\{\mu(X_a)\};
   \tag{2.4}
   \]
2. for \(a\ne b\),
   \[
   \lambda_U(a,b)\ne\lambda_U(b,a).
   \tag{2.5}
   \]

#### Proof

As \(b\) varies, the sets \(S_{ab}\) are all \(m\) lower facets of
\(X_a\). Properness at \(X_a\) gives \(m\) distinct colors, namely all
colors except its missing color. The two incidences in (2.5) meet at the
same lower vertex \(S_{ab}\), so properness there makes their colors
different. \(\square\)

Define

\[
 \boxed{
 \psi_U(\{a,b\})
 =\{\lambda_U(a,b),\lambda_U(b,a)\}.}
 \tag{2.6}
\]

This is well-defined as an unordered two-subset of \({\mathscr C}\).

### Theorem 2.2 (exact local fibre interpretation)

For every color pair \(p=\{\alpha,\beta\}\),

\[
 \boxed{
 h_p(U)
 =|\psi_U^{-1}(p)|
 =\#\{S\subset U:
 f_\alpha(S)\cup f_\beta(S)=U\}.}
 \tag{2.7}
\]

Moreover,

\[
 \sum_{p}h_p(U)=Q
 \qquad(U\in{\cal U}),
 \tag{2.8}
\]

and

\[
 \sum_{U}h_p(U)=N
 \qquad(p\in\binom{\mathscr C}2).
 \tag{2.9}
\]

#### Proof

Every \(S\subset U\) of rank \(m-1\) is uniquely \(S_{ab}\). Its two
middle extensions inside \(U\) are \(X_a,X_b\). The two distinguished
color extensions are exactly these two if and only if their incident
colors form \(p\), which is (2.7).

Equation (2.8) counts the \(Q\) domain pairs of \(\psi_U\). For fixed
\(p\), every \(S\in{\cal L}\) determines exactly one union
\(f_\alpha(S)\cup f_\beta(S)\in{\cal U}\), proving (2.9). \(\square\)

For fixed \(U,p\), orient every edge \(\{a,b\}\in\psi_U^{-1}(p)\) from
the endpoint carrying \(\alpha\) to the endpoint carrying \(\beta\).
By (2.4), every vertex has indegree at most one and outdegree at most one.
Therefore

\[
 \boxed{0\le h_p(U)\le n=m+1.}
 \tag{2.10}
\]

This bound is used in the near-Latin estimates below.

## 3. Exact holes, collisions, and averaging

For a fixed pair \(p\), define

\[
 H_p=|\{U:h_p(U)=0\}|,
 \qquad
 K_p=\sum_U(h_p(U)-1)_+.
 \tag{3.1}
\]

### Lemma 3.1 (global hole-collision identity)

For every \(p\),

\[
 \boxed{H_p=K_p,}
 \tag{3.2}
\]

and

\[
 \sum_U|h_p(U)-1|=2H_p.
 \tag{3.3}
\]

#### Proof

By (2.9), the \(N\) occurrences are distributed over exactly \(N\) upper
targets. Since \(h_p(U)\) is a nonnegative integer, its total deficit
below one is precisely the number of zero cells, and total deficit equals
total excess. \(\square\)

Likewise, at a fixed \(U\), define

\[
 \ell(U)=|\{p:h_p(U)=0\}|.
\]

Then

\[
 \ell(U)=\sum_p(h_p(U)-1)_+,
 \qquad
 \sum_p|h_p(U)-1|=2\ell(U).
 \tag{3.4}
\]

### Theorem 3.2 (exact defect averaging)

One has

\[
 \boxed{
 \sum_pH_p=\sum_U\ell(U)={\mathfrak L}(\kappa).}
 \tag{3.5}
\]

Equivalently, for a uniformly random color pair \(P\),

\[
 {\mathbb E}H_P={{\mathfrak L}(\kappa)\over Q}.
 \tag{3.6}
\]

Consequently

\[
 \min_pH_p\le
 \left\lfloor{{\mathfrak L}(\kappa)\over Q}\right\rfloor.
 \tag{3.7}
\]

In particular:

1. if \({\mathfrak L}(\kappa)<Q\), some pair is upper-perfect;
2. if \({\mathfrak L}(\kappa)\le\varepsilon QN\), some pair has at most
   \(\varepsilon N\) upper holes and the same collision excess;
3. if \({\mathfrak L}(\kappa)=o(QN)\), some pair has \(o(W)\) upper
   holes.

#### Proof

Both sides of (3.5) count pairs \((U,p)\) with \(p\notin
\operatorname {im}\psi_U\). Average over the \(Q\) color pairs and use
integrality. Since \(N=(1-o(1))W\), the last assertion follows. \(\square\)

There is an equivalent quadratic form. Put

\[
 {\cal Q}_p=\sum_U(h_p(U)-1)^2
\]

and

\[
 E(U)=\sum_p\binom{h_p(U)}2.
\]

Using (2.8)--(2.9),

\[
 \sum_p(h_p(U)-1)^2=2E(U),
 \tag{3.8}
\]

\[
 \sum_p{\cal Q}_p=2\sum_UE(U).
 \tag{3.9}
\]

The bound (2.10) gives the sharp-scale comparisons

\[
 2\ell(U)\le2E(U)\le n\ell(U),
 \tag{3.10}
\]

\[
 2H_p\le{\cal Q}_p\le nH_p.
 \tag{3.11}
\]

Thus quadratic defect \(o(N)\) is sufficient for \(o(N)\) holes, while
\(o(N)\) holes alone permits quadratic defect as large as
\(o(nN)\).

## 4. Missing-color margins

For \(U\in{\cal U}\) and \(c\in{\mathscr C}\), define

\[
 r_c(U)=|\{a\in U:\mu(X_a)=c\}|.
 \tag{4.1}
\]

The \(n\) values \(\mu(X_a)\) are the missing colors of the \(n\) middle
facets of \(U\).

### Theorem 4.1 (local pair-to-point margin identity)

For every \(U,c\),

\[
 \boxed{
 \sum_{p\ni c}h_p(U)=n-r_c(U).}
 \tag{4.2}
\]

Also,

\[
 \sum_cr_c(U)=n,\qquad
 \sum_Ur_c(U)=N.
 \tag{4.3}
\]

#### Proof

The left side of (4.2) counts half-edges of the local complete graph whose
label is \(c\). At vertex \(a\), the label \(c\) occurs exactly once if
\(\mu(X_a)\ne c\), and zero times otherwise, by (2.4). This proves
(4.2).

The first identity in (4.3) is immediate. For the second, each
\(X\in{\cal E}_c\) lies in exactly \(m\) upper sets, so

\[
 \sum_Ur_c(U)=m|{\cal E}_c|=mC=N.
\]

\(\square\)

Put

\[
 z_p(U)=h_p(U)-1,\qquad s_c(U)=r_c(U)-1.
 \tag{4.4}
\]

Then all row and column sums of both defect tables vanish, and (4.2)
becomes

\[
 \boxed{\sum_{p\ni c}z_p(U)=-s_c(U).}
 \tag{4.5}
\]

Thus a Latin pair row \(z_\bullet(U)=0\) forces the facet missing colors
to be a permutation, but the converse need not hold.

Define the missing-color support defect

\[
 \sigma(U)
 =n-|\{c:r_c(U)>0\}|
 =\sum_c(r_c(U)-1)_+
 ={1\over2}\sum_c|s_c(U)|.
 \tag{4.6}
\]

From (4.5) and (3.4),

\[
 \boxed{\sigma(U)\le2\ell(U).}
 \tag{4.7}
\]

Indeed, the unsigned incidence matrix of color pairs has column sum two,
so

\[
 \sum_c|s_c(U)|
 \le2\sum_p|z_p(U)|=4\ell(U).
\]

There is also a collision estimate. Let

\[
 B(U)=\sum_c\binom{r_c(U)}2
\tag{4.8}
\]

be the number of pairs of facets of \(U\) with the same missing color.
The unsigned vertex-edge incidence matrix of \(K_n\), restricted to
edge vectors of total sum zero, has squared operator norm \(n-2=m-1\):
indeed \(AA^{\mathsf T}=(n-2)I+J\), and the all-ones singular direction
is removed by the zero-sum condition.
Therefore (4.5), (3.10), and
\(\sum_cs_c(U)^2=2B(U)\) give

\[
 \boxed{
 B(U)\le{m^2-1\over2}\,\ell(U).}
 \tag{4.9}
\]

An elementary bound is sharper for \(m\ge3\). Since \(r_c(U)\le n\),

\[
 \binom{r_c(U)}2
 \le {n\over2}(r_c(U)-1)_+.
\]

Together with (4.7), this gives

\[
 \boxed{B(U)\le n\ell(U)=(m+1)\ell(U).}
 \tag{4.9a}
\]

These are one-way implications. Small pair-map defect forces small
missing-color defect, but balanced missing-color margins do not force a
Latin pair map.

There is also an exact global point-margin condition on the two missing
classes selected by a color pair. For
\(p=\{\alpha,\beta\}\), put

\[
 e_p(v)
 =|\{X\in{\cal E}_\alpha\cup{\cal E}_\beta:v\in X\}|.
\]

### Theorem 4.2 (selected missing-class point identity)

For every coordinate \(v\),

\[
 \boxed{
 e_p(v)-C
 =-\sum_{\substack{U\in{\cal U}\\v\in U}}(h_p(U)-1).}
 \tag{4.10}
\]

Consequently:

1. if \(p\) is upper-perfect, then
   \[
   e_p(v)=C\qquad(v\in[2m]);
   \tag{4.11}
   \]
2. for an arbitrary pair,
   \[
   |e_p(v)-C|\le2H_p.
   \tag{4.12}
   \]

#### Proof

For the Johnson edge generated by \(S\), with endpoints
\(f_\alpha(S),f_\beta(S)\) and union \(U(S)\), the incidence-vector
identity is

\[
 {\bf1}_{f_\alpha(S)}+{\bf1}_{f_\beta(S)}
 ={\bf1}_S+{\bf1}_{U(S)}.
\]

Sum over all \(S\). At a middle set \(X\), the left multiplicity is
\(2-{\bf1}_{\mu(X)\in p}\), so its coordinate-\(v\) total is
\(W-e_p(v)\). The lower and baseline upper coordinate totals sum to
\(N=W-C\). The deviation of the actual upper histogram from baseline is
the sum on the right of (4.10). Rearrangement proves (4.10), and (3.3)
gives (4.12). \(\square\)

Thus an exact distinguished pair already requires the union of its two
missing-color classes to be a point design. For \(m\ge2\), if every color
pair were exact, (4.11) for all pairs would force each individual
\({\cal E}_c\) to have coordinate degree \(C/2\); in particular \(C\)
would have to be even. Universal local Latinness imposes the still
stronger Steiner condition below.

## 5. The Steiner-resolution necessity

Call \(\kappa\) **universally local-Latin** when every \(\psi_U\) is a
bijection, equivalently

\[
 h_p(U)=1
 \quad(U\in{\cal U},\ p\in\binom{\mathscr C}2).
 \tag{5.1}
\]

### Theorem 5.1 (missing-color resolution equivalence and Latin necessity)

For the missing-color map of any proper \((m+1)\)-edge-coloring, the
following are equivalent.

1. For every \(U\), its \(n\) middle facets have all \(n\) missing colors:
   \[
   r_c(U)=1\qquad(c\in{\mathscr C}).
   \]
2. The map
   \[
   \mu:{\cal M}\longrightarrow{\mathscr C}
   \]
   is a proper \(n\)-coloring of the Johnson graph \(J(2m,m)\).
3. For every \(c\), the class \({\cal E}_c\) is a Steiner system
   \[
   S(m-1,m,2m),
   \tag{5.2}
   \]
   and the \(n=m+1\) systems form a large set partitioning all of
   \({\cal M}\).

Universal local Latinness implies all three conditions.

#### Proof

Equation (5.1) and the margin identity (4.2) give condition 1. Two
adjacent middle sets have a unique common union \(U\), so condition 1
implies condition 2.

Fix \(S\in{\cal L}\). Its \(n\) middle extensions form a clique in the
Johnson graph. Under condition 2 their missing colors are all distinct,
hence all colors occur once. Thus exactly one member of \({\cal E}_c\)
contains \(S\), which is condition 3. Conversely, condition 3 forbids two
same-color middle sets from sharing their \((m-1)\)-intersection, so it
implies condition 2. Condition 2 plainly makes the facets of each \(U\)
rainbow, giving condition 1. Lemma 1.1 supplies the asserted partition.
\(\square\)

### Corollary 5.2 (prime admissibility)

If a universally local-Latin proper coloring exists for \(m\ge2\), then

\[
 \boxed{m+1\text{ is prime}.}
 \tag{5.3}
\]

#### Proof

For a Steiner system \(S(m-1,m,2m)\), the number of blocks through a
fixed \((m-s)\)-set is

\[
 \lambda_{m-s}
 ={1\over s}\binom{m+s}{s-1}
 ={1\over m+1}\binom{m+s}s
 \qquad(1\le s\le m).
 \tag{5.4}
\]

Thus \(m+1\) must divide \(\binom{m+s}s\) for every \(s\).
Put \(n=m+1\). If \(n\) is composite and \(p\mid n\) is prime, take
\(s=p<n\). If \(p^a\Vert n\), then

\[
 v_p\binom{n-1+p}p=a-1,
 \tag{5.5}
\]

because among \(n,n+1,\ldots,n+p-1\) only \(n\) is divisible by \(p\),
while \(v_p(p!)=1\). Hence \(n\) does not divide the binomial
coefficient, a contradiction. \(\square\)

Primality is only a necessary divisibility condition; no existence is
claimed. The obstruction concerns all \(Q\) color pairs simultaneously
and does not by itself obstruct (0.10).

Moreover, every Steiner class forced here is automatically
complement-resolvable. Indeed, for a block \(B\in{\cal E}_c\), the number
of blocks disjoint from \(B\) is, by inclusion-exclusion,

\[
 d_0(B)=\sum_{i=0}^{m}(-1)^i\binom mi\lambda_i
 =(-1)^m+{1-(-1)^m\over m+1}.
 \tag{5.5a}
\]

For \(m\ge2\), prime \(m+1\) makes \(m\) even, so \(d_0(B)=1\). The only
\(m\)-set disjoint from \(B\) is \(B^c\); hence every
\({\cal E}_c\) splits into complementary parallel pairs
\(\{B,B^c\}\).

There is a quantitative composite-\(n\) residue version.

### Corollary 5.3 (composite residue defect floor)

Suppose \(n=m+1\) is composite and \(p<n\) is a prime divisor of \(n\).
Put

\[
 T_{m,p}=\binom{m+p}{p-1}.
 \tag{5.6}
\]

Then every proper \(n\)-edge-coloring satisfies

\[
 \boxed{
 {\mathfrak L}(\kappa)\ge{N\over2T_{m,p}}.}
 \tag{5.7}
\]

For odd \(m\ge3\), taking \(p=2\) gives

\[
 {\mathfrak L}(\kappa)\ge{N\over2(m+2)}.
 \tag{5.8}
\]

#### Proof

For \(c\in{\mathscr C}\) and \(S\in{\cal L}\), put

\[
 t_c(S)=|\{X\in{\cal E}_c:S\subset X\}|.
\]

Fix \(I\in\binom{[2m]}{m-p}\). If \(e_c(I)\) counts members of
\({\cal E}_c\) containing \(I\), then

\[
 \sum_{\substack{S\supset I\\|S|=m-1}}(t_c(S)-1)
 =p\,e_c(I)-T_{m,p}.
 \tag{5.9}
\]

Since \(m\equiv-1\pmod p\),
\(T_{m,p}\equiv1\pmod p\), so the absolute value in (5.9) is at least
one. Sum over \(I\). Each \(S\) contains
\(\binom{m-1}{p-1}\) such sets, and the factorial identity

\[
 {\binom{2m}{m-p}\over\binom{m-1}{p-1}}
 ={N\over T_{m,p}}
 \tag{5.10}
\]

gives

\[
 \sum_S|t_c(S)-1|\ge{N\over T_{m,p}}.
 \tag{5.11}
\]

Sum over all \(n\) colors. Half of this total absolute defect is positive
excess, and
\(\binom t2\ge(t-1)_+\). Counting same-missing-color Johnson edges first
by lower intersections and then by upper unions yields

\[
 {nN\over2T_{m,p}}
 \le\sum_UB(U).
\]

Finally (4.9a) gives
\(\sum_UB(U)\le n{\mathfrak L}(\kappa)\), proving (5.7).
\(\square\)

The normalized floor in (5.7) tends to zero after division by \(QN\).
It therefore does not force a linear number of holes for a distinguished
pair.

### Proposition 5.4 (resolved local margins are not sufficient)

Already for \(n=4\), the local properness rules admit a table with
pairwise distinct missing colors and a non-Latin pair map.

Take local vertices and colors \(1,2,3,4\), and set

\[
\begin{array}{c|ccc}
a&\multicolumn{3}{c}{b\mapsto\lambda(a,b)}\\ \hline
1&2\mapsto3&3\mapsto2&4\mapsto4\\
2&1\mapsto4&3\mapsto3&4\mapsto1\\
3&1\mapsto1&2\mapsto2&4\mapsto4\\
4&1\mapsto1&2\mapsto2&3\mapsto3.
\end{array}
\tag{5.12}
\]

Every row uses all colors except its row index, and opposite entries on
every unordered edge are distinct. Thus it satisfies exactly
(2.4)--(2.5), with \(\mu(X_a)=a\).

Its six pair images are

\[
 12\mapsto34,\quad
 13\mapsto12,\quad
 14\mapsto14,\quad
 23\mapsto23,\quad
 24\mapsto12,\quad
 34\mapsto34.
 \tag{5.13}
\]

Hence pairs \(13,24\) are missing and \(12,34\) occur twice. The
missing-color row is a permutation, but \(\ell(U)=2\).
\(\square\)

This is a local consistency example, not a claimed extension to a global
edge-coloring of \(H_3\). It proves that the point-margin identities and
even the exact local missing-color permutation required by a Steiner
resolution do not algebraically imply pair-map Latinness. It does not rule
out a separate global theorem deriving pair Latinness from a globally
consistent resolution and additional edge-coloring constraints.

## 6. Exact and near engine outputs

### Theorem 6.1 (distinguished-pair output)

For every proper \((m+1)\)-edge-coloring \(\kappa\), there is a color pair
\(p=\{\alpha,\beta\}\) whose suppressed Johnson pseudofactor has

1. every lower color exactly once;
2. middle degree one on
   \({\cal E}_\alpha\dot\cup{\cal E}_\beta\) and degree two elsewhere;
3. exactly \(C\) path components plus \(z_p\) cycle components;
4. at most
   \[
   \left\lfloor{{\mathfrak L}(\kappa)\over Q}\right\rfloor
   \tag{6.1}
   \]
   missing upper colors; and
5. exactly the same upper collision excess.

If \({\mathfrak L}(\kappa)<Q\), clauses 4--5 are zero. If
\({\mathfrak L}(\kappa)=o(QN)\), clauses 4--5 are \(o(W)\).

#### Proof

Choose \(p\) by Theorem 3.2. Proposition 1.2 gives clauses 1--3, and
Lemma 3.1 gives clause 5. \(\square\)

### Corollary 6.2 (exact/near Latin hierarchy)

The following conditions have sharply different strengths.

1. **One exact pair:**
   \[
   H_p=0.
   \]
   This is exactly two-sided q=1 rainbowness for the selected
   pseudofactor.
2. **One near pair:**
   \[
   H_p=o(W).
   \]
   This gives \(o(W)\) upper holes and collision excess, with exact lower
   colors and the fixed middle endpoint design.
3. **Average local near-Latinness:**
   \[
   {\mathfrak L}(\kappa)=o(QN).
   \]
   This is sufficient for condition 2 by averaging.
4. **Universal exact local Latinness:**
   \[
   {\mathfrak L}(\kappa)=0.
   \]
   This makes every color pair exact and forces the large-set Steiner
   resolution of Theorem 5.1.

No reverse implication from the missing-color margins to condition 4
follows locally, by Proposition 5.4. Nor does condition 3 imply an
asymptotically exact Steiner resolution: its allowed defect scale is
\(o(QN)\), whereas (4.7) yields a useful global missing-color conclusion
only at the much stronger scale \(o(N)\).

## 7. Precise surviving gate

The alternative coloring engine therefore reduces the q=1 construction
to the following concrete target.

> Construct a proper \((m+1)\)-edge-coloring of \(H_m\) with
> \({\mathfrak L}(\kappa)=o(QN)\), and find a distinguished color pair
> attaining both \(H_p=o(W)\) and
> \[
> z_p=o(W/H)
> \]
> bichromatic cycles.

The first demand gives near two-sided color coverage by Theorem 6.1. The
second is independent component control. The \(C=W/(m+1)\) forced paths
already satisfy \(C=o(W/H)\) whenever \(H=o(m)\).

What is proved here is the exact local map, all point and pair margins,
the finite defect-averaging inequality, the Steiner necessity of universal
Latinness, and the exact/near hierarchy. What is not proved is a coloring
with subaverage local defect, a compatible low-cycle pair, or any
higher-depth chronology. The universal Steiner obstruction cannot be
used to rule out this weaker distinguished-pair route.
