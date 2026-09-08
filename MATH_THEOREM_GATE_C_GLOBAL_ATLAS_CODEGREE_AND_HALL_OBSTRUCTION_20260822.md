# Gate C: exact global-atlas codegrees and the support-compatible Hall obstruction

**Status (2026-08-22).**  Every theorem in this note is proved.  The note
does not construct a near-spanning absorber-domain atlas.  It identifies
the exact quantitative boundary faced by such a construction, proves the
largest routing atlas supplied by the elementary orbit-avoidance argument,
and separates ordinary Hall expansion from the stronger simultaneous
support condition.

Let

\[
 b=2h+1\ge 7,\qquad
 \mathcal V={\Omega\choose b},\qquad
 W=|\mathcal V|={2b\choose b}.
\]

We use the explicit binary absorber domain from the one-to-two identity.
On a fixed split \(\Omega=A\mathbin{\dot\cup}B\), with
\(|A|=|B|=b\), its support can be
written

\[
 D=\mathcal F\boxtimes\mathcal Y,
 \qquad \mathcal F=\mathcal D_0\mathbin{\dot\cup}\mathcal D_2,
 \qquad |\mathcal F|=2b,\quad |\mathcal Y|=b,                 \tag{0.1}
\]

where \(\mathcal D_0,\mathcal D_2\) are the two disjoint decks of
cyclic \(h\)-intervals displayed below, \(\mathcal Y\) is any cyclic
deck of \((h+1)\)-intervals on \(B\), and

\[
 \mathcal F\boxtimes\mathcal Y
 :=\{X\cup Y:X\in\mathcal F,\ Y\in\mathcal Y\}.                \tag{0.1a}
\]

\[
 |D|=s=2b^2.                                                 \tag{0.2}
\]

The **labelled domain-orbit hypergraph** \(\mathcal H_D\) has vertex set
\(\mathcal V\) and one labelled edge \(gD\) for every
\(g\in\operatorname{Sym}(\Omega)\).  Equal supports with different
labels are retained.

The principal conclusions are as follows.

1.  \(\mathcal H_D\) is regular of degree

    \[
                         d_*=2b^2(b!)^2.                       \tag{0.3}
    \]

    Its exact maximum pair codegree is

    \[
       \boxed{
       {\Delta_2(\mathcal H_D)\over d_*}
          ={4+17/b\over b^2},}                                \tag{0.4}
    \]

    attained precisely by pairs at Johnson distance one.  Hence

    \[
       \boxed{
       s{\Delta_2(\mathcal H_D)\over d_*}=8+{34\over b}.}      \tag{0.5}
    \]

    The relative codegree tends to zero, but the edge-size-weighted
    parameter does not.

2.  Every maximal disjoint domain atlas has at least

    \[
                         {W\over4b^4}                           \tag{0.6}
    \]

    domains.  Consequently any already disjoint family of \(m\) source
    domains extends to \(m\) further, collectively disjoint port domains
    whenever

    \[
                         2m\le {W\over4b^4}.                    \tag{0.7}
    \]

    In that range the transporter graph is complete and all \(m\)
    transports are simultaneously support-compatible.

3.  Ordinary Hall expansion is not the remaining issue once the source
    and port shores are individually disjoint.  If there are \(m\)
    disjoint source supports and \(q\ge m\) disjoint ports, all of size at
    most \(s\) and \(s\), respectively, then their disjointness graph has
    a left-saturating matching as soon as \(q\ge2s\).  However, if a
    transport uses the full union of its source support and its port,
    simultaneous support compatibility is equivalent to selecting \(m\)
    ports disjoint from the union of *all* source supports.  Cardinality
    alone guarantees this only under

    \[
                         q\ge m(s+1).                            \tag{0.8}
    \]

    This bound is sharp using only disjointness and support sizes.

4.  A disjoint atlas of \((1-o(1))W/(2b^2)\) domains would itself give a
    product-atom matching covering \((1-o(1))W\) middle vertices: put
    every domain in its two-atom state.  Thus the requested near-spanning
    atlas is already a near-factor theorem, not an auxiliary consequence
    of the local absorber.

These statements isolate the positive missing input.  One must either
prove a matching theorem using more of the explicit domain geometry than
the maximum-codegree row, or jointly construct the preliminary leave and
the source/port supports so that the cross-support loss in (0.8) does not
occur.  The results below do not prove that such a construction is
impossible.

## 1. Orbit codegrees from the internal distance census

For \(S,T\in\mathcal V\), write

\[
                         \partial(S,T)=|S-T|.                    \tag{1.1}
\]

For a family \(K\subseteq\mathcal V\), let

\[
 m_d(K)=|\{(X,Y)\in K^2:\partial(X,Y)=d\}|,
 \qquad n_d(K)={m_d(K)\over |K|}.                               \tag{1.2}
\]

Thus \(n_d(K)\) is the average number of members of \(K\) at distance
\(d\) from one of its members.

### Lemma 1.1 (orbit codegree formula)

The vertex degree of the labelled orbit hypergraph of a nonempty family
\(K\subseteq\mathcal V\), \(|K|=k\), is

\[
                              d_K=k(b!)^2.                       \tag{1.3}
\]

For two distinct vertices at distance \(d\), its codegree \(\lambda_d(K)\)
satisfies

\[
        \boxed{
        {\lambda_d(K)\over d_K}
        ={n_d(K)\over {b\choose d}^2}.}                         \tag{1.4}
\]

#### Proof

There are \((2b)!k\) labelled edge--vertex incidences.  Transitivity on
the \(W\) middle vertices gives

\[
 d_K={(2b)!k\over W}=k(b!)^2,
\]

which is (1.3).

Fix ordered pairs \((X,Y)\) and \((S,T)\), both at distance \(d\).
Their four Venn cells have sizes \(b-d,d,d,b-d\), so exactly

\[
                         (d!)^2((b-d)!)^2                         \tag{1.5}
\]

coordinate permutations send \((X,Y)\) to \((S,T)\).  Summing (1.5)
over the \(m_d(K)\) ordered internal pairs gives

\[
 \lambda_d(K)=m_d(K)(d!)^2((b-d)!)^2.
\]

Divide by \(d_K=k(b!)^2\) and use
\(b!/(d!(b-d)!)={b\choose d}\).  This proves (1.4). \(\square\)

## 2. The exact distance-one census of the absorber domain

Label \(A=\{0,1,\ldots,2h\}\), put

\[
                         w=h-1,\qquad u=2h-1,\qquad v=2h,        \tag{2.1}
\]

and take

\[
 \alpha_0=(0,1,\ldots,2h),
\]

\[
 \alpha_2=(u,h-2,h-3,\ldots,0,
                 h,h+1,\ldots,2h-2,v,w).                       \tag{2.2}
\]

Let \(\mathcal D_i\) be the deck of cyclic \(h\)-intervals of
\(\alpha_i\).  These two decks are disjoint.  To audit the only special
distance counts needed below, write the members of \(\mathcal D_2\) as

\[
 X=\{0,\ldots,h-2,u\},
 \qquad Y=\{h,\ldots,2h-2,v\},                                  \tag{2.3}
\]

\[
 S_a=\{0,\ldots,h-a-1\}\cup\{h,\ldots,h+a-1\}
                    \quad(1\le a\le h-1),                      \tag{2.4}
\]

\[
 T_a=\{h-a+1,\ldots,h-1\}\cup\{h+a,\ldots,2h\}
                    \quad(2\le a\le h-1),                      \tag{2.5}
\]

and

\[
 U=\{w,v\}\cup\{h+1,\ldots,2h-2\},
 \qquad V=\{1,\ldots,h-1,u\}.                                  \tag{2.6}
\]

There are \(2+(h-1)+(h-2)+2=2h+1=b\) sets in this list.
Let

\[
                         N_i=\{i,i+1,\ldots,i+h-1\}\pmod b      \tag{2.7}
\]

be the members of \(\mathcal D_0\).  Direct comparison of endpoints in
(2.3)--(2.7) gives the following complete table.  A blank entry means
that there is no such \(N_i\).

\[
\begin{array}{c|c|c}
 Z&\{i:|Z-N_i|=1\}&\{i:|Z-N_i|=h\}\\ \hline
 X&\{0,b-2,b-1\}&\{h-1\}\\
 Y&\{h-1,h,h+1\}&\{0\}\\
 S_1&\{0,1,b-1\}&\{h+1\}\\
 S_{h-1}&\{h-1,h\}&\\
 T_2&\{h+1,h+2\}&\\
 U&\{h-1,h+1\}&\\
 V&\{0,1\}&\\
 S_a\ (2\le a\le h-2)&&\\
 T_a\ (3\le a\le h-1)&&
\end{array}                                                   \tag{2.8}
\]

The same endpoint comparison proves
\(\mathcal D_0\cap\mathcal D_2=\varnothing\): every set in
(2.3)--(2.6) has at least two components in the natural cyclic order,
whereas each \(N_i\) is one cyclic interval. Thus the disjoint-union
notation in (0.1) is justified internally.

For completeness, (2.8) can be checked without a picture.  Each exceptional
set in (2.3), (2.6), and the three exceptional parameter rows is the union
of the displayed ordinary integer intervals.  Intersecting it with (2.7),
and splitting \(N_i\) at zero only when \(i+h-1\ge b\), gives exactly the
listed start indices.

It remains only to justify the blank parameter rows.  For
\(2\le a\le h-2\), the two cyclic runs of \(S_a\) have lengths
\(h-a,a\), both at least two, and its two complementary gaps have lengths
\(a,h-a+1\), both below \(h\).  No length-\(h\) interval is therefore
disjoint from \(S_a\).  Such an interval either stays in one run, in which
case it misses the other run of at least two points, or meets both runs, in
which case it must cross a gap of at least two points and again cannot
contain more than \(h-2\) of the \(h\) points of \(S_a\).  Thus its
intersection size is neither zero nor \(h-1\).  For
\(3\le a\le h-1\), the corresponding run lengths of \(T_a\) are
\(a-1,h-a+1\), and its gap lengths are \(a,h-a+1\); all four are at
least two except that the gaps need only be below \(h\), which they are.
The identical argument applies.  The omitted endpoint values of \(a\)
are exactly the exceptional rows already displayed.  Thus (2.8) is an
exhaustive endpoint calculation, not an experimental assertion.

It follows immediately that the number of ordered pairs
\((N,Z)\in\mathcal D_0\times\mathcal D_2\) at distances one and \(h\)
is respectively

\[
                              17\quad\hbox{and}\quad3.           \tag{2.9}
\]

### Lemma 2.1 (local shell averages)

For \(\mathcal F=\mathcal D_0\mathbin{\dot\cup}\mathcal D_2\), write
\(a_p=n_p(\mathcal F)\).  Then

\[
 a_1=2+{17\over b},\qquad a_h=2+{3\over b},
 \qquad \sum_{p=0}^h a_p=2b.                                  \tag{2.10}
\]

For the cyclic deck \(\mathcal Y\) of \((h+1)\)-intervals, write
\(c_q=n_q(\mathcal Y)\).  Then

\[
 c_0=1,\qquad c_q=2\quad(1\le q\le h).                         \tag{2.11}
\]

#### Proof

In any cyclic deck on \(b=2h+1\) points, a fixed interval has exactly two
deck intervals at each positive Johnson distance \(1,\ldots,h\).  Hence
each of \(\mathcal D_0,\mathcal D_2\) contributes \(2b\) ordered pairs
at distances one and \(h\).  Equation (2.9), in the two ordered
directions, adds \(34\) and \(6\), respectively.  Division by
\(|\mathcal F|=2b\) gives the first two identities in (2.10).  The final
identity simply says that every member of \(\mathcal F\) has all \(2b\)
members, including itself, distributed among the distance shells.

The same cyclic-shift count, with the interval length complemented, gives
(2.11). \(\square\)

### Theorem 2.2 (exact maximum pair codegree)

For the absorber domain \(D=\mathcal F\boxtimes\mathcal Y\),

\[
             \max_{1\le d\le b}
             {n_d(D)\over {b\choose d}^2}
             ={4+17/b\over b^2},                               \tag{2.12}
\]

and the maximum is attained exactly at \(d=1\).  Consequently (0.3)--(0.5)
hold.

#### Proof

Johnson distance is additive across the disjoint coordinate blocks in
the Cartesian product.  Therefore

\[
                         n_d(D)=\sum_{p+q=d}a_pc_q.              \tag{2.13}
\]

Equations (2.10)--(2.11) give

\[
 n_1(D)=a_1+c_1=4+{17\over b},                                  \tag{2.14}
\]

and, since \(b-1=2h\),

\[
 n_{b-1}(D)=a_hc_h=4+{6\over b}.                               \tag{2.15}
\]

For \(2\le d\le b-2\), use \(c_q\le2\) and (2.10) in (2.13):

\[
                         n_d(D)\le2\sum_pa_p=4b.                \tag{2.16}
\]

Also \({b\choose d}\ge{b\choose2}\) in this range, so

\[
 {n_d(D)\over{b\choose d}^2}
 \le {16\over b(b-1)^2}
 <{4+17/b\over b^2}.                                            \tag{2.17}
\]

For the last strict inequality, the direct common-denominator calculation is

\[
 {16\over b(b-1)^2}<{4b+17\over b^3}
 \quad\Longleftrightarrow\quad
 {16b^2\over(b-1)^2}<4b+17,                                    \tag{2.18}
\]

and the left side is at most \(16(7/6)^2<22\), while the right side is
at least \(45\).  Finally, (2.15) divided by \(b^2\) is strictly below
(2.14) divided by \(b^2\).  The only remaining distinct-pair distance is
\(d=b\), i.e. complementation. Every member of \(D\) has split
\((h,h+1)\) across \((A,B)\), while its complement has split
\((h+1,h)\), so \(n_b(D)=0\). Thus (2.12) holds over all pair distances.

Apply Lemma 1.1 with \(k=s=2b^2\).  It gives
\(d_*=s(b!)^2\), (0.4), and after multiplication by \(s\), (0.5).
\(\square\)

The displayed value is an inherent boundary term: every constituent
product atom already gives each of its vertices four distance-one
neighbours.  Thus changing the cross-deck part of the absorber cannot make
the edge-size-weighted pair parameter vanish while the domain still
contains two whole product atoms.

There is also a full-codegree endpoint obstruction to direct use of a
generic all-codegrees hierarchy.  Every nonempty simple orbit hypergraph
has full-edge codegree at least one, while its degree is at most \(d_*\).
Thus any parameter constrained by

\[
                         B\le(d_*/C_s)^{1/(s-1)}                 \tag{2.19}
\]

obeys

\[
 B\le d_*^{1/(2b^2-1)}
   =\exp\left\{{\log b-1\over b}
          +O\left({\log b\over b^2}\right)\right\}
   =1+O\left({\log b\over b}\right).                          \tag{2.20}
\]

Equations (0.5) and (2.20) are obstructions to those black-box criteria,
not to an explicit integral packing.

## 3. The unconditional sparse atlas

### Lemma 3.1 (avoidance of a fixed used set)

For every \(U\subseteq\mathcal V\), a uniformly random labelled orbit
copy \(gD\) satisfies

\[
                         \mathbb E|gD\cap U|={s|U|\over W}.      \tag{3.1}
\]

In particular, if \(s|U|<W\), some orbit copy is disjoint from \(U\).

#### Proof

For each fixed \(X\in D\), the image \(gX\) is uniform on
\(\mathcal V\), so its probability of lying in \(U\) is \(|U|/W\).
Sum over the \(s\) members of \(D\).  If every copy met \(U\), the
integer-valued intersection size would always be at least one, contradicting
(3.1) when its right side is below one. \(\square\)

### Theorem 3.2 (maximal and extendible sparse atlases)

Every maximal pairwise-disjoint family of domain copies has size at least

\[
                              {W\over s^2}={W\over4b^4}.         \tag{3.2}
\]

More generally, every already disjoint domain family can be extended until
its size is at least \(\lceil W/s^2\rceil\).

#### Proof

If the current family has \(q<W/s^2\) members, its used union \(U\) has
size \(qs\), and

\[
                              {s|U|\over W}={qs^2\over W}<1.
\]

Lemma 3.1 supplies a further disjoint copy.  Iterate.  A maximal family
therefore cannot have size below \(W/s^2\). \(\square\)

### Corollary 3.3 (complete sparse routing atlas)

Suppose \(K_1,\ldots,K_m\) are already pairwise-disjoint copies of the
binary domain.  If

\[
                         2m\le\left\lceil{W\over4b^4}\right\rceil,          \tag{3.3}
\]

then there are further domain copies \(D_1,\ldots,D_m\) such that all
\(2m\) supports are pairwise disjoint.  Every source domain can be paired
with every port domain, so the packet-transporter graph is \(K_{m,m}\),
and every routing matching is simultaneously support-compatible.

#### Proof

Apply the extension assertion of Theorem 3.2 to the source family and
retain any \(m\) newly added domains as ports.  Collective disjointness
makes every two-domain transporter legal and makes the supports belonging
to distinct selected pairs disjoint. \(\square\)

The guaranteed number of routed \(b^2\)-packets in (3.3) is only
\(W/(8b^4)+O(1)\), hence its guaranteed hole volume is only
\(W/(8b^2)+O(b^2)\).  This is a positive theorem, but it is below the
current polynomial-density preliminary leaves. It concerns the undoubled
domains \(D\). A complement-safe switch uses
\(D\mathbin{\dot\cup}\overline D\); cross-intersections
\(D_i\cap\overline{D_j}\) need not vanish, so (3.3) does not itself give a
doubled complement-safe atlas.

## 4. Ordinary Hall versus simultaneous support compatibility

The next theorem is abstract and therefore applies to every realization
of the packet transporter whose support is the union of one source domain
and one port domain.

Let \(K_1,\ldots,K_m\) be pairwise-disjoint source supports with
\(|K_i|\le s\), and let \(D_1,\ldots,D_q\) be pairwise-disjoint port
supports with \(|D_j|=s\).  Join \(K_i\) to \(D_j\) when they are
disjoint.

### Theorem 4.1 (automatic ordinary Hall expansion)

If

\[
                              q\ge m\quad\hbox{and}\quad q\ge2s,           \tag{4.1}
\]

then the disjointness graph has a matching saturating all \(m\) source
supports.

#### Proof

Because the ports are disjoint, a fixed \(K_i\) meets at most
\(|K_i|\le s\) of them.  Hence every source has at least \(q-s\)
neighbours.

Let \(X\) be a nonempty source subfamily.  If \(|X|\le q-s\), the
neighbourhood of any one member already gives \(|N(X)|\ge q-s\ge|X|\).
If \(|X|>q-s\) and a port \(D_j\) lay outside \(N(X)\), then it would
meet every source in \(X\).  The sources are disjoint, so these
intersections use distinct points of \(D_j\), forcing \(|X|\le s\).
But \(q\ge2s\) gives \(q-s\ge s\), a contradiction.  Thus in the second
case \(N(X)\) is the entire set of \(q\) ports and
\(|N(X)|=q\ge m\ge|X|\).  Hall's condition holds in both cases. \(\square\)

### Theorem 4.2 (exact clean-port criterion)

Assume that the transporter assigned to a legal pair \((K_i,D_j)\) uses
no vertices outside \(K_i\cup D_j\), uses that whole set as its certified
support, and is legal only when \(K_i\cap D_j=\varnothing\).  Then legal
injections \(\phi:[m]\to[q]\) whose \(m\) transporter supports

\[
                              K_i\cup D_{\phi(i)}                 \tag{4.2}
\]

are pairwise disjoint exist if and only if at least \(m\) ports avoid

\[
                              K=\bigcup_{i=1}^m K_i.              \tag{4.3}
\]

In particular the number of clean ports is at least

\[
                              q-|K|\ge q-ms,                      \tag{4.4}
\]

so

\[
                              \boxed{q\ge m(s+1)}                 \tag{4.5}
\]

is a universal sufficient condition.  No smaller bound follows from the
support sizes and the two within-shore disjointness assumptions alone.

#### Proof

Legality makes every selected port disjoint from its assigned source.  If
the unions in (4.2) are pairwise disjoint, it is also disjoint from every
other source; hence it avoids \(K\).  Conversely, any \(m\) distinct ports avoiding \(K\),
paired arbitrarily with the sources, give pairwise-disjoint unions because
both shores are individually disjoint.  This proves the equivalence.

Every dirty port contains a point of \(K\).  Since the ports are pairwise
disjoint, choosing one such point from each dirty port injects the dirty
ports into \(K\).  This proves (4.4), and (4.5) makes its right side at
least \(m\).

For sharpness using only these abstract data, take \(m\) disjoint
\(s\)-sets \(K_i\).  Make \(ms\) disjoint port supports, each meeting
\(K\) in a different one of its \(ms\) points, filling the rest of each
port with fresh points.  Add only \(m-1\) clean ports.  Then
\(q=m(s+1)-1\), but there are only \(m-1\) clean ports, so simultaneous
support-compatible routing is impossible. \(\square\)

Thus Theorem 4.1 can certify an excellent ordinary Hall graph while
Theorem 4.2 still fails.  For a hypothetical near-spanning port atlas
\(q=(1-o(1))W/s\), the universal clean-port guarantee reaches only

\[
                              m\lesssim {W\over s^2}={W\over4b^4},          \tag{4.6}
\]

the same scale as the elementary sparse atlas.  To route many more packets,
one needs a joint construction proving that the actual source union meets
far fewer than \(ms\) ports, or a transporter implementation whose
auxiliary supports can overlap without causing atom conflicts.  Ordinary
Hall density by itself cannot supply either fact.

## 5. Why a near-spanning domain atlas is already the near-factor

### Proposition 5.1 (atlas-to-atom-factor implication)

If \(D_1,\ldots,D_q\) are pairwise-disjoint copies of the binary domain,
then there is a matching of \(2q\) genuine all-split product atoms covering
exactly their union.  Consequently, if

\[
                         q=(1-o(1)){W\over2b^2},                 \tag{5.1}
\]

then the all-split product-atom hypergraph has a matching covering
\((1-o(1))W\) vertices.

#### Proof

Each domain has the on-state decomposition

\[
                              D_i=E_{i,0}\mathbin{\dot\cup}E_{i,2}          \tag{5.2}
\]

into two genuine product atoms.  The domains are disjoint, so all \(2q\)
atoms in (5.2) are mutually disjoint.  They cover \(q|D|=2b^2q\)
vertices.  Substitution of (5.1) proves the final assertion. \(\square\)

This explains the precise status of Gate C's global request.  The local
one-to-two and three-to-three identities solve the algebra of absorption
and transport.  A near-spanning disjoint support atlas would solve the
integral middle-layer packing problem itself.  Its proof must therefore be
a genuinely new coordinated packing theorem, not a formal consequence of
the already proved local switches or of the ordinary Hall criterion.

## 6. Mechanical audit

The companion verifier

`scratch/verify_gate_c_global_atlas_codegree_20260822.py`

constructs \(\mathcal D_0,\mathcal D_2,\mathcal F,\mathcal Y\) for every
odd \(b=7,\ldots,41\), and constructs the full Cartesian domain through
\(b=25\).  It verifies the complete cross-deck table (2.8), the counts
\(17,3\), the convolution (2.13), and the exact maximizing value (2.12).
It is a finite audit of the formulas, not a substitute for the proofs
above.
