# XOR transverse mosaics beyond one hash: rigidity, a frame-dependent orthogonal library, and the exact shallow gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
                 G=\mathbb F_2^\ell,\qquad |G|=2m,
                 \qquad W=\binom{2m}{m},
                 \qquad N_q=\binom{2m}{m-q}.
\tag{0.1}
\]

Throughout the exact dyadic calculations we take \(\ell\ge3\), so
\(m=2^{\ell-1}\) is divisible by four.  This is the regime of the
asymptotic construction; it also fixes the sign in the exact middle
XOR-fibre formula used below.

The XOR-addressed transverse mosaic from
`MATH_THEOREM_O_XOR_HASH_TRANSVERSE_MOSAIC_AND_Q4_HIERARCHY_OBSTRUCTION_20260726.md`
uses the rainbow frame-label set

\[
                       \mathcal A=K\times\{1\},
                       \qquad |\mathcal A|=m,
\tag{0.2}
\]

and one translation matching

\[
                       M_a=\{\{x,x+a\}:x\in G\}/2
\tag{0.3}
\]

for every \(a\in\mathcal A\).  Its owner leave is
\(O(W/m)+e^{-\Omega(m)}W=o(W/H)\) whenever \(H=o(m)\).

This report attacks the two remaining gates: literal collisions between
different XOR status cells and the old logarithmic Fourier cutoff.  The
conclusions are sharp but do not prove coefficient one.

1. **Globally compatible orthogonal hashes are rigid.**  Let
   \(h_\Phi(X)=\sum_{x\in X}\Phi(x)\) be any incidence-linear hash.  If
   its increment is direction-homogeneous on every retained frame of the
   fixed XOR atlas, then either it is an affine image of the old XOR
   \(\sigma(X)=\sum_{x\in X}x\), or it is compatible with at most
   \(m/4\) of the \(m\) frames.  In the latter case retaining only
   compatible frame fibres forces owner leave at least

   \[
                         {3\over4}\left(W-\binom m{m/2}\right)
                         =\left({3\over4}-o(1)\right)W.
   \tag{0.4}
   \]

   Thus no single new joint two-shore-compatible hash family can preserve
   the required leave \(o(W/H)\).  In the affine case, on each fixed rank,
   an arbitrary family still has joint rank at most
   \(\ell=\log_2(2m)\) and cannot refine literal targets inside a
   \(\sigma\)-fibre.
2. **The obstruction is not a universal multihash no-go.**  A genuinely
   frame-dependent library exists.  For \(R=2^d\), split the coordinates
   into \(2R\) equal linear atoms and, for a frame macro-direction \(v\),
   record the \(R\) parities paired by \(v\).  The resulting hash is
   exactly constant on every full status cell of that frame, has
   \(R-1\) independent bits on the middle layer, and two distinct frame
   hashes have joint rank

   \[
                              {3R\over2}-1.
   \tag{0.5}
   \]

   Taking \(R\asymp\log m\) supplies \(\Theta(\log m)\) stable bits per
   frame with exponentially small distributional error.  No theorem here
   converts those bits into the required negative physical covariance.
3. **There is an exact common-owner multiframe atlas.**  Partition the
   XOR address space into even blocks \(S_i\).  For every perfect matching
   of each \(S_i\), pairing two hash values \(s,s'\) and using ground frame
   \(M_{s+s'}\) partitions the same owner slab
   \(\{X:\sigma(X)\in S_i\}\) exactly into full status cells.  Hence
   different frame matchings really are integral options on common owner
   blocks; they are not merely a fractional mixture.  A rainbow partition
   into nonparallel four-hash blocks makes every option an all-transverse
   \(Q_r\)-nearfactor with uniform leave
   \(O(W/m)+e^{-\Omega(m)}W=o(W/H)\).  Their target covariance remains
   unproved.
4. **Depth one has no star or coarse Hall deficit.**  If \(\tau\) is the
   address involution and \(T\) is an \((m-1)\)-target, its compatible
   transitions are exactly the \(\tau\)-pairs internal to one canonical
   \((m+1)\)-set.  Every such target has at least one provider.  The
   paired lower/upper target graph is asymptotically regular and has Hall
   deficiency \(o(W)\).
5. **A literal depth-one endpoint packing exists.**  A fixed-rank
   near-regular hypergraph matching theorem gives \(W-o(W)\) selected
   physical transitions whose lower colours are all distinct, whose upper
   colours are all distinct, and whose middle-owner degree is at most two.
   This is stronger than hash-bin balance.  It is not yet a cyclic factor:
   the number of components is uncontrolled, the quantitative owner-slot
   leave is not shown to be \(o(W/H)\), and depths \(q\ge2\) are absent.
6. **Independent orthogonal product laws are rigorously excluded.**  At
   every depth \(q=o(\sqrt m)\) with diffuse cell marginals, independent cell choices
   leave at least

   \[
                              (e^{-1}-o(1))N_q
   \tag{0.6}
   \]

   expected targets uncovered.  Through \(q\le40\log m\), the integral
   floor reserve is only \(o(W)\); a successful law must therefore cancel
   essentially the entire diagonal cell self-energy, which is
   \(\Theta(W)\) per diffuse tagged row, by negative cross-cell covariance.
   Compatible hash orthogonality contributes no such term.

The exact surviving problem is a correlated whole-configuration Hall
selection, simultaneously for both signs and every \(2\le q\le H\),
followed by a small-component cyclic completion.  No positive-density
literal Hall witness against that unrestricted correlated problem is
proved here.  In particular, this report does not prove `CPM`, MWB, or the
coefficient-one theorem.

## 1. The exact all-depth configuration dual

Let \(\mathscr C\) be any retained owner-disjoint family of literal status
cells.  For a cell \(C\), let \(\mathcal O_C\) be its finite menu of legal
factor states.  One state means one complete common choice at every depth,
not a depthwise marginal.  Index tagged targets by

\[
                 t=(q,\varepsilon,T),\qquad
                 1\le q\le H,\quad\varepsilon\in\{-,+\},
\tag{1.1}
\]

and let \(a_{C,o,t}\) be the literal occurrence multiplicity of \(t\) in
state \(o\).  The fractional minimum-hole programme is

\[
\begin{aligned}
 \eta=\min\quad&\sum_tz_t,\\
 z_t+\sum_{C,o}a_{C,o,t}x_{C,o}&\ge1 &&(t),\\
 \sum_{o\in\mathcal O_C}x_{C,o}&=1 &&(C),\\
 x_{C,o},z_t&\ge0.
\end{aligned}
\tag{1.2}
\]

### Theorem 1.1 (literal configuration Hall dual)

The exact dual of (1.2) is

\[
 \boxed{
 \eta=
 \max_{0\le y_t\le1}
 \left[
   \sum_ty_t-
   \sum_{C\in\mathscr C}\max_{o\in\mathcal O_C}
               \sum_ta_{C,o,t}y_t
 \right].}
\tag{1.3}
\]

If \(L\) owners are discarded and subsequently granted arbitrary
favourable traces, a full-mass dual witness of value \(D\) still proves

\[
                              \eta\ge D-2HL.
\tag{1.4}
\]

#### Proof

Give the covering inequalities in (1.2) dual variables \(y_t\ge0\), and
the cell equalities free dual variables \(\beta_C\).  The \(z_t\)-columns
give \(y_t\le1\).  The \(x_{C,o}\)-columns give

\[
                       \beta_C+\sum_ta_{C,o,t}y_t\le0.
\tag{1.5}
\]

For fixed \(y\), maximize by taking

\[
                       \beta_C=-\max_o\sum_ta_{C,o,t}y_t,
\tag{1.6}
\]

which proves (1.3) by finite-dimensional linear-programming duality.

One owner contributes at most one occurrence at each of the \(2H\)
tagged ranks.  Since \(0\le y_t\le1\), granting arbitrary service from
one discarded owner can lower the dual payoff by at most \(2H\).  Sum
over the \(L\) owners to obtain (1.4). \(\square\)

For the XOR leave

\[
                      L=O(W/m)+e^{-\Omega(m)}W,
\tag{1.7}
\]

the correction in (1.4) is \(o(W)\) for every \(H=o(m)\).  Thus a
linear dual witness cannot be hidden in the known owner quarantine.

At one fixed rank with chronology removed there is no analogous
fractional obstruction.  In the unrestricted inclusion graph between
middle owners and rank \(m-q\), owner degree is \(\binom mq\), target
degree is \(\binom{m+q}q\), and uniform edge weight
\(1/\binom mq\) gives target load

\[
 {\binom{m+q}q\over\binom mq}={W\over N_q}.
\tag{1.8}
\]

The obstruction in (1.3) is precisely that every one-rank flow must arise
from the same legal cyclic cell state.

## 2. Rigidity of globally frame-compatible incidence hashes

For an \(\mathbb F_2\)-space \(B\) and an arbitrary map
\(\Phi:G\to B\), put

\[
                         h_\Phi(X)=\sum_{x\in X}\Phi(x).
\tag{2.1}
\]

Define its constant-derivative direction set

\[
 C_\Phi=
 \{a\in G:\Phi(x+a)+\Phi(x)\text{ is independent of }x\}.
\tag{2.2}
\]

Direction homogeneity is the compatibility used by an additive
packet-phase hash: every flip of an \(M_a\)-edge must change the hash by
one value depending on \(a\), not on the physical edge.

### Lemma 2.1 (constant-derivative dichotomy)

The set \(C_\Phi\) is a linear subspace of \(G\).  Moreover, either
\(C_\Phi=G\) and \(\Phi\) is affine, or

\[
                         \operatorname {codim}C_\Phi\ge2.
\tag{2.3}
\]

#### Proof

If \(a,b\in C_\Phi\), then

\[
 D_{a+b}\Phi(x)=D_a\Phi(x+b)+D_b\Phi(x)
\tag{2.4}
\]

is constant.  Hence \(C_\Phi\) is a subspace, and its derivative constants
form a linear map on that subspace.

Suppose \(C=C_\Phi\) has codimension one, and choose \(v\notin C\).  If
the derivative homomorphism is \(L:C\to B\), then

\[
 \Phi(c)=\Phi(0)+L(c),\qquad
 \Phi(v+c)=\Phi(v)+L(c)\qquad(c\in C).
\tag{2.5}
\]

It follows that \(D_v\Phi\) is the constant
\(\Phi(v)+\Phi(0)\), contrary to \(v\notin C_\Phi\).  Thus a proper
constant-derivative subspace has codimension at least two.  If
\(C_\Phi=G\), (2.5) with \(C=G\) says exactly that \(\Phi\) is affine.
\(\square\)

### Theorem 2.2 (the sharp fixed-atlas \(3/4\) obstruction)

Assume one joint hash \(h_\Phi\) is required to have a homogeneous
increment on every retained frame of the fixed explicit XOR atlas, and
that owners in incompatible frame fibres are discarded rather than
reassigned or retiled.  Then either

\[
                         \Phi(x)=c+Lx
\tag{2.6}
\]

for a linear map \(L\), or the owner leave obeys

\[
                         \boxed{
 L_{\rm owner}\ge{3\over4}\left(W-\binom m{m/2}\right).}
\tag{2.7}
\]

#### Proof

Write \(\mathcal A=\{a:\lambda(a)=1\}\), where \(\lambda\) is the
last-coordinate functional.  If \(C_\Phi\) is proper, Lemma 2.1 gives
\(|C_\Phi|\le|G|/4=m/2\).  Either
\(C_\Phi\subseteq\ker\lambda\), in which case its intersection with
\(\mathcal A\) is empty, or \(\lambda|_{C_\Phi}\) is nonzero, in which
case

\[
                  |\mathcal A\cap C_\Phi|={|C_\Phi|\over2}\le{m\over4}.
\tag{2.8}
\]

The explicit address involution uses every label \(a\in\mathcal A\)
exactly once.  Its frame fibre consists of two middle XOR fibres.  With

\[
                         C_m=\binom m{m/2},
\tag{2.9}
\]

Fourier inversion on the additive group \(G\), using \(m\equiv0\pmod4\),
gives

\[
 \#\{X:|X|=m,\sigma(X)=0\}
 ={W+(2m-1)C_m\over2m},\qquad
 \#\{X:|X|=m,\sigma(X)=s\}
 ={W-C_m\over2m}\quad(s\ne0).
\]

Indeed every nontrivial character has \(m\) positive and \(m\) negative
coordinates, and its middle coefficient is
\([z^m](1-z^2)^m=C_m\).  Thus every pair of distinct hash fibres has at
least

\[
                            {W-C_m\over m}
\tag{2.10}
\]

owners.  At least \(3m/4\) frame labels are incompatible, so discarding
their fibres proves (2.7).  If \(C_\Phi=G\), Lemma 2.1 gives (2.6).
\(\square\)

The scope in Theorem 2.2 is essential.  It does not cover different
hashes on disjoint frame slabs, a union of compatible subspaces, an
edge-dependent increment, or literal retiling of the incompatible
owners.  Those are new physical routers rather than a globally compatible
extension of the old XOR hash.

### Corollary 2.3 (all compatible hashes factor through \(\sigma\))

For affine \(\Phi(x)=c+Lx\), every rank-\(k\) target satisfies

\[
                  h_\Phi(T)=L\sigma(T)+(k\bmod2)c.
\tag{2.11}
\]

Consequently, on each fixed rank, an arbitrary family of hashes compatible
with every frame has joint rank at most \(\ell\), not the sum of its
advertised output dimensions.  It is a deterministic function of
\(\sigma(T)\) and the known rank parity.  Across both rank parities one
additional parity bit may occur through the affine constants.

If such a hash is required to be constant, rather than merely
direction-homogeneous, on every selected full status cell, then all its
derivatives on \(\mathcal A\) vanish.  The prescribed-active-edge lemma
for the XOR atlas realizes every ground edge of every label in
\(\mathcal A\); since \(\mathcal A\) spans \(G\), \(L=0\).  Thus no
nontrivial globally linear cell identifier exists.

There is a separate address-level collapse which does not use linearity.
Suppose a joint address takes values \(s\) in an \(\mathbb F_2\)-space,
a ground frame \(a(s)\) is chosen from the address alone, and flipping an
edge of that frame changes the address by a nonzero value
\(\Delta(a(s))\) depending only on the frame.  Exact cell stability forces

\[
                       a\bigl(s+\Delta(a(s))\bigr)=a(s).
\tag{2.12}
\]

Consequently

\[
                       F(s)=s+\Delta(a(s))
\tag{2.13}
\]

is one fixed-point-free involution of the joint address image:

\[
                       F^2(s)=s.
\tag{2.14}
\]

Conversely, such an involution is sufficient only when its displacement
\(F(s)+s\) is constant on every address fibre assigned the same physical
frame and that displacement is realized by the frame label.  Thus adding
compatible address coordinates does not overlay several
independent frame fields.  It merely replaces the original \(\tau\) by
one involution on a possibly relabelled quotient.

## 3. Rank and Fourier blindness

The preceding rigidity has an exact information-theoretic version.

### Lemma 3.1 (dimension of the compatible function space)

Let \(U\le G\) have dimension \(d\) and codimension
\(c=\ell-d\).  The scalar maps \(\phi:G\to\mathbb F_2\) satisfying

\[
                        D_u\phi(x)\text{ is constant in }x
                        \qquad(u\in U)
\tag{3.1}
\]

form a vector space of exact dimension

\[
                                  d+2^c.
\tag{3.2}
\]

#### Proof

Choose a section \(G=U\oplus V\).  Every such map is uniquely

\[
                         \phi(u+v)=L(u)+g(v),
\tag{3.3}
\]

where \(L\in U^*\) and \(g:V\to\mathbb F_2\) is arbitrary.  Conversely
every map (3.3) has the required constant derivatives.  The two free
spaces have dimensions \(d\) and \(2^c\). \(\square\)

For \(B\)-valued maps, multiply (3.2) by \(\dim B\).  Formula (3.2) is
the dimension of the entire available scalar row space, not a claim that
an arbitrary chosen family attains that rank.  If a positive-density set
of frame directions is required, then \(d=\ell-O(1)\), so the compatible
row space is only \(O(\log m)\)-dimensional.

### Lemma 3.2 (central-layer linear separation needs rank \(2m-2\))

Let \(A:\mathbb F_2^{2m}\to\mathbb F_2^r\) be linear and injective on
all characteristic vectors of one rank \(k=m\pm q\), where

\[
                              1\le q<{m\over3}.
\tag{3.4}
\]

Then

\[
                                  \boxed{r\ge2m-2.}
\tag{3.5}
\]

#### Proof

Suppose \(r\le2m-3\).  The kernel has dimension at least three, and its
intersection with the even-weight hyperplane has dimension at least two.
Choose independent even words \(u,v\) there.  The three nonzero words
\(u,v,u+v\) obey

\[
 |u|+|v|+|u+v|
   =2|\operatorname {supp}u\cup\operatorname {supp}v|
   \le4m.
\tag{3.6}
\]

One therefore has even weight \(2t\le4m/3<2(m-q)\).  Split its support
into two \(t\)-sets and adjoin the same \((k-t)\)-set outside its support.
This is possible for both \(k=m-q\) and \(k=m+q\), since
\(t\le\min\{k,2m-k\}\).  The resulting distinct \(k\)-sets have
difference in \(\ker A\), contradicting injectivity. \(\square\)

Thus even an unrestricted collection of \(\ell\)-bit binary linear hashes
needs at least \((2m-2)/\ell\) independent members merely to separate one
central rank.  Compatible hashes are much weaker because their joint row
space is bounded by Lemma 3.1.

There is also a concrete blind trade.  If \(u\ne0\) is a common
homogeneous direction, then every compatible vector hash assigns the same
sum to every full \(u\)-edge:

\[
             \Phi(x)+\Phi(x+u)=\Phi(y)+\Phi(y+u).
\tag{3.7}
\]

Replacing one full edge by another is invisible.  More generally, fix the
split edges and their orientations in an \(M_u\)-status, and fix that
exactly \(f\) of the remaining \(m-s\) edges are full.  All

\[
                                  \binom{m-s}{f}
\tag{3.8}
\]

choices of those full edges have the same joint compatible-hash signature.
At central parameters this blind class is exponential in \(m\).

Finally, stable-hash marginals cannot certify literal coverage even when
they are perfectly balanced.  Choose one target \(T_t\) in each nonempty
\(\sigma\)-fibre and put the entire correct fibre load on \(T_t\).  Every
compatible hash total is identical to that of a uniform literal load, but
the number of holes is

\[
                 \#\{\text{holes}\}\ge N_k-2m=(1-o(1))N_k.
\tag{3.9}
\]

This is the explicit Fourier-invisibility obstruction: all compatible
characters lie in the fibre-constant subspace, whose dimension is at most
\(2m\), while its orthogonal complement has dimension at least
\(N_k-2m\).

At depth one the compatible-hash marginal is already exact.  The
translation-equivariant factor choice from the preceding XOR theorem has,
for retained owner mass \(S=W-L\),

\[
                   Z_{1,t}^{\varepsilon,\sigma}={S\over2m}
                   \qquad(t\in G,\ \varepsilon\in\{-,+\}).
\tag{3.10}
\]

The target demand in every XOR fibre is \(N_1/(2m)\).  Pushing (3.10)
through any compatible affine hash therefore gives total two-sided hash
deficit exactly

\[
                         2(N_1-S)_+\le2L.
\tag{3.11}
\]

Thus the logarithmic cutoff is absent at \(q=1\) at every compatible
hash level.  What remains invisible is precisely the literal distribution
inside those balanced bins.

## 4. A frame-dependent orthogonal hash library

Theorem 2.2 concerns one joint hash required to work on all frames.  The
following construction shows exactly how frame-dependent projections
escape it.

Choose independent linear forms, with \(1\le d\le\ell-1\),

\[
                  b,\mu_1,\ldots,\mu_d:G\longrightarrow\mathbb F_2,
                  \qquad R=2^d,
\tag{4.1}
\]

and write \(\mu=(\mu_1,\ldots,\mu_d)\).  Thus

\[
                  \mathcal A=\{a:b(a)=1\}.
\tag{4.2}
\]

Partition the ground coordinates into the \(2R\) atoms

\[
 A_{\epsilon,z}
   =\{x:b(x)=\epsilon,\ \mu(x)=z\},
 \qquad |A_{\epsilon,z}|={m\over R}.
\tag{4.3}
\]

For a set \(X\), let

\[
                       P_{\epsilon,z}(X)
                       =|X\cap A_{\epsilon,z}|\pmod2.
\tag{4.4}
\]

If \(a\in\mathcal A\), put

\[
                       v(a)=(1,\mu(a))\in\mathbb F_2^{d+1}.
\tag{4.5}
\]

Translation by \(a\) pairs atom \(u\) with atom \(u+v(a)\).  Define
the frame projection

\[
 H_a(X)=
 \left(P_u(X)+P_{u+v(a)}(X)\right)_
 {u\in\mathbb F_2^{d+1}/\langle v(a)\rangle}.
\tag{4.6}
\]

### Theorem 4.1 (exact stable pair-parity hashes)

The hashes in (4.6) have the following properties.

1. \(H_a\) is exactly constant on every full \(M_a\)-status cell.
2. On the middle layer it has rank \(R-1\).
3. If \(v(a)\ne v(a')\), then

   \[
                   \operatorname {rank}(H_a,H_{a'})={3R\over2}-1.
   \tag{4.7}
   \]

   Thus the second frame contributes exactly \(R/2\) new bits beyond
   the first.
4. For a uniformly chosen middle owner, its atomic parity vector is
   within total variation

   \[
                   2^{2R}(2m+1)2^{-m/R}
   \tag{4.8}
   \]

   of the uniform distribution on its forced even-parity hyperplane.

#### Proof

Flipping one \(M_a\)-edge toggles precisely the two atom parities indexed
by \(u,u+v(a)\).  Their sum is fixed, proving Item 1.

Let \(E\le\mathbb F_2^{2R}\) be the even-parity hyperplane of atomic
parity vectors.  The kernel of \(H_a|_E\) consists of vectors constant on
the \(R\) pairs of the matching generated by \(v(a)\).  It has dimension
\(R\); hence

\[
                         \operatorname {rank}H_a
                         =(2R-1)-R=R-1.
\tag{4.9}
\]

For independent nonzero \(v,w\), the common kernel consists of vectors
constant on every coset of \(\langle v,w\rangle\).  There are \(R/2\)
such four-point cosets, and the global even-parity relation is automatic
on them.  Therefore

\[
              \operatorname {rank}(H_v,H_w)
              =(2R-1)-{R\over2}={3R\over2}-1,
\tag{4.10}
\]

proving Items 2 and 3.

For Item 4, a Fourier character of the atomic parity vector corresponds
to the parity of the intersection with a union \(B\) of atoms.  Modulo the
forced all-atom character, a nontrivial character may be represented with

\[
                         {m\over R}\le|B|\le m.
\tag{4.11}
\]

Its conditional Fourier coefficient on the middle layer is

\[
 { [z^m](1-z)^{|B|}(1+z)^{2m-|B|}
      \over \binom{2m}m}.
\tag{4.12}
\]

Writing the numerator as
\((1-z^2)^{|B|}(1+z)^{2m-2|B|}\), its coefficient absolute value is at
most \(2^{2m-|B|}\).  Since
\(\binom{2m}m\ge2^{2m}/(2m+1)\), (4.11) bounds every nontrivial Fourier
coefficient by \((2m+1)2^{-m/R}\).  Summing over fewer than
\(2^{2R}\) characters proves (4.8). \(\square\)

Taking \(R\asymp\log m\) makes (4.8) equal
\(2^{-\Omega(m/\log m)}\) and gives \(\Theta(\log m)\) stable bits per
frame.  These are real physical status-cell invariants, not affine copies
of \(\sigma\).  They are necessarily frame-dependent, as Theorem 2.2
predicts.

The theorem does not say that two different values of \(H_a\) correspond
to disjoint physical target spaces.  Nor does it choose a factor based on
these values.  In particular, the rank computation (4.7) is an
information resource, not the negative covariance theorem required by
the configuration dual.

## 5. Common owner blocks with exact multiframe options

There is an exact way to put different frame matchings on the same owner
mass.

Let

\[
                         G=S_1\dot\cup\cdots\dot\cup S_b
\tag{5.1}
\]

be any partition into even sets.  Define the common owner slabs

\[
                         \Omega_i
                          =\{X\in\tbinom Gm:\sigma(X)\in S_i\}.
\tag{5.2}
\]

For each \(i\), let \(\pi_i\) be an arbitrary perfect matching of the
hash vertices in \(S_i\).

### Theorem 5.1 (hash-slab option atlas)

For an edge \(p=\{s,s'\}\in\pi_i\), put \(a_p=s+s'\).  The full
\(M_{a_p}\)-status cells of owners having hash \(s\) or \(s'\) partition
\(\Omega_i\) exactly into literal variable-dimensional orientation cubes.
Consequently every tuple \((\pi_1,\ldots,\pi_b)\) is an exact owner
partition of the whole middle layer, and every \(\Omega_i\) has the full
perfect-matching menu \(\operatorname {PM}(S_i)\) on the same owner set.
Complementation preserves every option.

#### Proof

Fix \(p=\{s,s'\}\) and put \(a=s+s'\).  Flipping any split edge of
\(M_a\) changes the middle XOR by \(a\), so the full status cell of an
owner of hash \(s\) has all its hashes contained in

\[
                              \{s,s+a\}=\{s,s'\}.
\tag{5.3}
\]

The containment is equality when the cell has positive dimension; a
zero-dimensional cell is a singleton.  This distinction does not affect
the partition argument.

Every owner in that cell therefore remains in \(\Omega_i\).  As in the
basic XOR cell-stability proof, two selected full status cells belonging
to the same pair are equal or disjoint and exhaust the two hash fibres.
Different edges of \(\pi_i\) have disjoint hash pairs, so their cells are
disjoint.  They exhaust all hashes in \(S_i\), proving the first claim.
The slabs in (5.1) are disjoint and exhaustive, proving the global claim.
Finally \(\sigma(G\setminus X)=\sigma(X)\), and complementation exchanges
full with empty status while preserving split status. \(\square\)

This theorem is a genuine common-block construction of the kind needed by
a Latin packet-resolution argument.  It also shows why Theorem 2.2 must
not be overstated: incompatible owners can be retiled by changing the hash
matching itself.

The theorem alone supplies no fixed packet dimension.  For any particular
option, the usual concentration estimate makes the owner mass in cells of
dimension below \(m/3\) exponentially small.  Such low cells can be paid
inside that option, but the low-cell sets depend on \(\pi_i\); no common
option-independent quarantine with the same bound is proved here.  More
importantly, the target incidence arrays of different perfect-matching
options have not been shown to obey the Latin floor-covariance inequality.

There is one immediate statewise no-go.  Suppose the blocks \(S_i\) are
the affine cosets of one two-dimensional subspace \(U\le G\), and the
three options on each four-set are its three translation matchings.  Every
selected hash-pair difference then lies in \(U\).  Hence every physical
ground swap \(x\leftrightarrow x+a\) stays inside one ground-coordinate
coset of \(U\).  The entire option atlas is again internal to the fixed
four-block decomposition by those cosets.  The full-block Gaussian Hall
cut therefore survives every Latin coupling and every factor phase.  A
surviving use of Theorem 5.1 must employ nonparallel blocks or matchings
whose differences cross a fixed four-block decomposition on positive
owner mass.

That owner-side requirement can be met exactly.

We use the following elementary slice concentration estimate here and
again below.  If \(X\) is a uniform \(k\)-subset of an \(n\)-set and
\(f\) changes by at most \(c\) when one selected point is exchanged for
one unselected point, then

\[
 \Pr(|f(X)-\mathbb Ef(X)|\ge t)
 \le 2\exp\left(-{t^2\over8kc^2}\right).
\]

Indeed, expose a uniformly random ordered sample without replacement
whose first \(k\) entries form \(X\).  Conditional completions after a
change in one exposed entry can be coupled by one exchange, so the Doob
martingale increment has range at most \(2c\); Azuma gives the displayed
bound.  Its constant is deliberately nonoptimal.  Azuma's inequality is
used here as a standard imported concentration theorem.

### Theorem 5.2 (rainbow four-hash option nearfactors)

Fix an old partition of the ground coordinates into four-blocks.  Let

\[
 B=\{a\ne0:M_a\text{ has more than }m/12
                    \text{ old-block-internal edges}\}.
\tag{5.4}
\]

Then \(|B|<36\).  There is a partition of the hash space \(G\) into
four-sets for which only \(O(1)\) hash blocks contain any pair of
difference in \(B\).  After discarding the corresponding common owner
slabs, every one of the three perfect-matching options on every retained
hash block has the following property: for every \(2\le r\le m/4\), all
but

\[
                         e^{-\Omega(m)}W
\tag{5.5}
\]

owners can be partitioned into all-transverse literal \(Q_r\)-packets.
The mass in (5.5) is the additional option-dependent low-cell leave
inside the retained common slabs.  Including the contaminated common
slabs, the total active-packet owner leave, uniformly over every global
option vector, is

\[
                         O(W/m)+e^{-\Omega(m)}W=o(W/H)
                         \qquad(H=o(m)).
\tag{5.6}
\]

The option-dependent exceptional status cells may instead be retained as
singleton/null packets, so every option remains an exact tiling of its
full common owner slab.  No common option-independent low-dimensional
quarantine is asserted.

#### Proof

The count of old internal coordinate pairs gives

\[
                         \sum_{a\ne0}i(a)=3m,
\tag{5.7}
\]

so (5.4) has fewer than \(36\) elements.  Choose a uniformly random
partition of the \(2m\) hash vertices into four-sets.  A fixed unordered
hash pair lies in one block with probability \(3/(2m-1)\).  Each bad
difference supplies \(m\) pairs, so the expected number of bad-pair
incidences internal to the random hash blocks is at most

\[
                    |B|m{3\over2m-1}=O(1).
\tag{5.8}
\]

Some partition therefore has only \(O(1)\) contaminated blocks.  Their
four-hash owner slabs have total mass \(O(W/m)+e^{-\Omega(m)}W\), by the
exact XOR-fibre formula.

Every edge of every perfect matching on a retained four-set has difference
outside \(B\).  Hence its ground frame has at most \(m/12\) old-internal
edges.  For a fixed selected frame, the number \(D_a(X)\) of split edges
has the usual middle-slice tail

\[
                         \Pr(D_a<m/3)\le e^{-\Omega(m)}.
\tag{5.9}
\]

For any global option vector there are only \(m\) selected hash-pair
frames.  A union bound, including the polynomial XOR-conditioning factor,
keeps the total owner mass in its low-dimensional full status cells at
\(e^{-\Omega(m)}W\), uniformly over the option vector.  In every other
cell,

\[
 \#\{\text{split axes crossing old blocks}\}
 \ge {m\over3}-{m\over12}={m\over4}.
\tag{5.10}
\]

Choose any \(r\) of those axes and freeze the rest to obtain the asserted
parallel \(Q_r\)-subdivision.  Low-dimensional cells are whole cells for
the selected option because \(D_a\) is constant on an \(M_a\)-status
cell; they may be declared leave or tiled by singleton/null packets.  This
proves (5.5)--(5.6) without claiming that the low-cell identity is common
to different options. \(\square\)

Theorem 5.2 clears owner conflicts and the old fixed-four-block cut for a
whole multiframe option library.  It does not control which literal
targets different hash blocks emit, so it supplies neither (1.3) nor
(10.13).

For reference, if options \(o\) are installed on the common blocks and
\(d_{i,o,t}\) denotes their complete tagged target tower, a permutation
coupling has load

\[
                              Z_t(\rho)=\sum_i d_{i,\rho(i),t}.
\tag{5.11}
\]

The exact negative terms in its second moment are row and column squares
of the array \((d_{i,o,t})\).  Constructing the matchings \(\pi_i\) so
that those negative terms cancel the cell self-energy at every signed
depth is precisely the unresolved Latin router; arbitrary or independent
perfect matchings do not have the required sign.

## 6. Exact depth-one target geometry

Return to one fixed-point-free address involution \(\tau:G\to G\).  Let

\[
                         \mathcal P=\{\{s,\tau(s)\}:s\in G\}/2
\tag{6.1}
\]

be its perfect matching on the hash space.  The frame belonging to
\(p=\{s,\tau(s)\}\) has difference

\[
                              a_p=s+\tau(s).
\tag{6.2}
\]

### Lemma 6.1 (lower and upper provider matchings)

For \(T\in\binom G{m-1}\), put \(t=\sigma(T)\).  The selected-cell
transitions whose lower trace is \(T\) are in bijection with

\[
                 p\in\mathcal P\quad\text{such that}\quad
                 t+p\subseteq G\setminus T.
\tag{6.3}
\]

The corresponding two middle owners are

\[
                 T\cup\{t+s\},\qquad
                 T\cup\{t+\tau(s)\}.
\tag{6.4}
\]

For \(U\in\binom G{m+1}\), with \(t=\sigma(U)\), the upper providers
are exactly

\[
                 p\in\mathcal P\quad\text{such that}\quad
                 t+p\subseteq U.
\tag{6.5}
\]

Complementary lower and upper targets have identical provider sets.

#### Proof

If \(p=\{s,\tau(s)\}\) satisfies (6.3), the two added coordinates in
(6.4) are absent from \(T\), differ by \(a_p\), and the two owners have
hashes

\[
                       t+(t+s)=s,
                       \qquad t+(t+\tau(s))=\tau(s).
\tag{6.6}
\]

They are opposite endpoints of an active \(M_{a_p}\)-edge in one selected
status cell, and their intersection is \(T\).  Conversely, if a selected
cell edge has lower trace \(T\), its two owner hashes form one
\(\tau\)-pair, and solving (6.6) recovers (6.4).  This proves (6.3).
The union calculation is identical and gives (6.5).  Since the total XOR
of \(G\) is zero, complementation preserves the target XOR and exchanges
the two criteria. \(\square\)

Canonical translation removes the moving target hash.  Put

\[
                         \widehat T=T+\sigma(T).
\tag{6.7}
\]

Because \(|T|=m-1\) is odd,

\[
                         \sigma(\widehat T)=0.
\tag{6.8}
\]

Thus the lower provider degree is the number of \(\tau\)-edges contained
in the zero-XOR \((m+1)\)-set

\[
                         A_T=G\setminus\widehat T.
\tag{6.9}
\]

The upper canonical form is the same.

### Corollary 6.2 (no isolated depth-one target)

Every lower and every upper depth-one target has at least one selected-cell
provider.

#### Proof

For any perfect matching on \(2m\) points and any \((m+1)\)-set \(A\),
let \(g,o,c\) be the numbers of matching edges internal to \(A\), internal
to its complement, and crossing.  Then

\[
                         2g+c=m+1,
                         \qquad2o+c=m-1.
\tag{6.10}
\]

Hence \(g=o+1\ge1\).  Apply this to (6.9) and to the upper analogue.
\(\square\)

The complete degree distribution before the zero-XOR conditioning is also
explicit.  The number of \((m+1)\)-sets containing exactly \(j\) internal
edges of a fixed perfect matching is

\[
 A_{m,j}
   =\binom mj\binom{m-j}{j-1}2^{m-2j+1}.
\tag{6.11}
\]

Indeed, choose the \(j\) internal edges, the \(j-1\) edges internal to
the complement, and one endpoint of every remaining crossing edge.  In
particular the minimum-degree class has size only

\[
                         A_{m,1}=m2^{m-1}.
\tag{6.12}
\]

There is a useful uniform concentration form.  If \(A\) is an unrestricted
uniform \((m+1)\)-set and \(g(A)\) counts internal matching edges, then

\[
 \mathbb E g(A)
   =m{(m+1)m\over(2m)(2m-1)}
   ={m(m+1)\over2(2m-1)}={m\over4}+O(1).
\tag{6.13}
\]

Slice bounded differences gives, for every \(\delta_m\to0\) with
\(\delta_m^2m/\log m\to\infty\),

\[
 \Pr\left(|g(A)-\mathbb Eg|>\delta_mm\right)
       \le e^{-\Omega(\delta_m^2m)}.
\tag{6.14}
\]

At odd rank the XOR fibres are exactly uniform, so conditioning on
\(\sigma(A)=0\) costs a factor exactly \(2m\).  Consequently all but

\[
                       b_mN_1,
                       \qquad
                       b_m=2m e^{-\Omega(\delta_m^2m)}=o(1),
\tag{6.15}
\]

targets on either shore have provider degree in \([d_-,d_+]\), where

\[
 \mu_m={m(m+1)\over2(2m-1)},\qquad
 d_-:=\mu_m-\delta_mm,\qquad d_+:=\mu_m+\delta_mm.
\tag{6.16}
\]

The transfer from canonical zero-XOR sets to targets is uniform: each
zero-XOR \((m+1)\)-set has exactly \(2m\) translated target preimages.
Indeed a nonzero translation has two-point coordinate orbits and hence
cannot stabilize an odd-cardinality set.  Thus (6.15) is a target census,
not merely a census of canonical representatives.

The absolute maximum is \((m+1)/2\).

## 7. The paired-colour Hall graph

Let \(\Gamma_\tau\) be the graph of all selected-status-cell Johnson
edges.  Define the bipartite graph \(B_\tau\) with left vertex set
\(\binom G{m-1}\), right vertex set \(\binom G{m+1}\), and one edge

\[
                  \bigl(X\cap Y,\ X\cup Y\bigr)
\tag{7.1}
\]

for every \(XY\in E(\Gamma_\tau)\).  It is simple because a lower/upper
pair determines its two middle vertices.  Put

\[
                         \nu_\tau=\nu(B_\tau),
                         \qquad\Delta_\tau=N_1-\nu_\tau.
\tag{7.2}
\]

### Theorem 7.1 (the depth-one Hall deficiency is sublinear)

For every fixed-point-free address involution \(\tau\),

\[
                              \boxed{\Delta_\tau=o(W).}
\tag{7.3}
\]

#### Proof

Complementation is a degree-preserving isomorphism between the two
shores of \(B_\tau\).  Use \(\delta_m\) as in (6.14), and call the
\(b_mN_1\) exceptional vertices on either side bad.  For a left set
\(S\) and its neighborhood \(R\), edge counting gives

\[
 d_-\bigl(|S|-b_mN_1\bigr)
 \le d_+|R|+{m+1\over2}b_mN_1.
\tag{7.4}
\]

Therefore

\[
 |S|-|R|
 \le
 \left(1-{d_-\over d_+}\right)N_1
 +
 \left({d_-\over d_+}+{m+1\over2d_+}\right)b_mN_1
 =O(\delta_m+b_m)N_1=o(W).
\tag{7.5}
\]

The maximum of \(|S|-|N(S)|\) is the bipartite Hall deficiency, proving
(7.3). \(\square\)

There is an exact necessary connection to a physical owner factor whose
transitions all lie in \(\Gamma_\tau\).  If such a factor uses \(S_0\)
owner-start occurrences and leaves \(M^-_1,M^+_1\) targets uncovered,
choose one transition representative for every covered lower target and
one for every covered upper target.  The two
representative sets have intersection at least

\[
                         2N_1-M^-_1-M^+_1-S_0.
\tag{7.6}
\]

Their common representatives have both lower and upper colours distinct,
and hence form a matching in \(B_\tau\).  Thus

\[
 \boxed{
 M^-_1+M^+_1
   \ge2N_1-S_0-\nu_\tau
   =N_1-S_0+\Delta_\tau.}
\tag{7.7}
\]

Theorem 7.1 says that (7.7) supplies no linear obstruction.  It does not
construct a common set of physical transitions under the middle-owner
degree and cycle constraints.

## 8. A literal depth-one partial router

The coarse Hall theorem can be strengthened to a simultaneous physical
endpoint packing.  We use the following standard fixed-uniformity form of
the fractional nibble theorem.

> **Fractional-nibble theorem.**  Fix \(k\).  Let \(\mathcal H_n\) be
> \(k\)-uniform hypergraphs carrying fractional matchings \(w_n\).  If
> \(\max_e w_n(e)=o(1)\), every pair of vertices has total common-edge
> weight \(o(1)\), and \(\sum_e w_n(e)=M_n\), then
> \(\mathcal H_n\) has an integral matching of size
> \((1-o(1))M_n\).

This is the usual fixed-rank semi-random matching theorem in its
fractional form.  It is an imported theorem; no growing-uniformity claim
is being made.

Clone every middle owner twice.  Form a four-uniform hypergraph
\(\mathcal H_1\) with vertex set

\[
 \binom G{m-1}\ \dot\cup\ \binom G{m+1}\
 \ \dot\cup\ \left(\binom Gm\times\{1,2\}\right).
\tag{8.1}
\]

For each valid selected-cell transition \(XY\), and each
\(i,j\in\{1,2\}\), put in the hyperedge

\[
 \{X\cap Y,\ X\cup Y,\ (X,i),\ (Y,j)\}.
\tag{8.2}
\]

### Theorem 8.1 (simultaneous depth-one endpoint packing)

The hypergraph \(\mathcal H_1\) has a matching of size

\[
                                  W-o(W).
\tag{8.3}
\]

After projection to physical Johnson edges, this gives a family with

* pairwise distinct lower targets;
* pairwise distinct upper targets;
* middle-owner degree at most two; and
* only \(o(W)\) uncovered lower targets, upper targets, and owner clones.

#### Proof

If a lower or upper target has provider count \(g\), its degree in
\(\mathcal H_1\) is \(4g\).  By (6.13)--(6.16), all but \(o(W)\)
targets have degree

\[
                                  m+o(m).
\tag{8.4}
\]

For an owner \(X\), let \(D(X)\) be the number of split edges in its
addressed translation matching.  Each owner clone lies in two hyperedges
for every active neighbor, so its degree is \(2D(X)\).  For a fixed frame,
\(D\) has mean

\[
                                  {m^2\over2m-1}={m\over2}+O(1)
\tag{8.5}
\]

on the middle slice and has exponential linear-deviation tails.
Conditioning on the adaptive XOR fibre costs only a polynomial factor;
the union bound over the \(2m\) frames therefore shows that all but
\(o(W)\) owner clones also have degree

\[
                                  m+o(m).
\tag{8.6}
\]

Absolute degrees are at most \(2m+2\).  The maximum pair-codegree is four:
a lower/upper pair determines at most one physical transition and four
clone choices; a target and an owner clone leave at most two choices for
the other clone; two owner clones determine at most one transition; and
same-shore target pairs never co-occur.

Let \(B\) be the \(o(W)\) exceptional vertices and delete every hyperedge
meeting \(B\).  This removes at most \(o(Wm)\) hyperedges.  The remaining
four-graph \(\mathcal H'_1\) satisfies

\[
 \begin{aligned}
 |E(\mathcal H'_1)|&=(1-o(1))Wm,\\
 \Delta(\mathcal H'_1)&\le(1+o(1))m,\\
 \Delta_2(\mathcal H'_1)&\le4.
 \end{aligned}
\tag{8.7}
\]

Put \(D_m=\Delta(\mathcal H'_1)\) and give every remaining edge weight

\[
                                  w(e)={1\over D_m}.
\tag{8.8}
\]

This is a fractional matching.  Also

\[
 4|E(\mathcal H'_1)|
 \le |V(\mathcal H'_1)|D_m,
\]

so (8.7) and \(|V(\mathcal H'_1)|\le2N_1+2W=(4-o(1))W\)
give \(D_m\ge(1-o(1))m\).  Together with
\(D_m\le(1+o(1))m\), this shows \(D_m=(1+o(1))m\).  Its total
weight is at least

\[
                                  W-o(W),
\tag{8.9}
\]

and every vertex pair has common-edge weight \(O(1/m)=o(1)\).  The
fractional-nibble theorem gives (8.3).

Two hyperedges over the same physical transition share both its lower and
upper vertices, so a matching projects to distinct physical transitions.
The two target coordinates give the two injectivity statements, and the
two clones bound every middle-owner degree by two. \(\square\)

The limitations of Theorem 8.1 are substantial and exact.

1. The qualitative clone deficit \(o(W)\) is not the required
   \(o(W/H)\) owner leave.
2. The projected graph is only maximum-degree two.  It is not proved to
   extend to a two-factor inside the pre-existing XOR status cells.
3. A path with two deficient endpoints may contain \(\Theta(W)\) owners,
   so deleting noncyclic components is invalid.
4. The number of cycles and paths is uncontrolled and can be
   \(\Theta(W)\), causing a linear collar charge.
5. No cyclic \(H\)-geodesicity or depth \(q\ge2\) trace statement follows.
6. Completing paths or joining cycles can destroy both distinct-colour
   ledgers.

Thus (8.3) is a genuine literal positive result at depth one, not a hidden
claim of a factor or contiguous-OR word.

## 9. The independent-choice Poisson obstruction

The failure of independent hash choices is architecture-free once each
cell has a diffuse target menu.

Let cells choose independently.  At one tagged rank, let
\(Y_{C,T}\in\{0,1\}\) indicate that cell \(C\) emits target \(T\), and
put

\[
 p_{C,T}=\Pr(Y_{C,T}=1),\qquad
 \eta=\max_{C,T}p_{C,T},\qquad
 S=\sum_{C,T}p_{C,T}.
\tag{9.1}
\]

Here \(S\) is the expected total within-cell distinct-image mass at that
rank.  It is at most the owner-occurrence mass, and equals it when every
cell state is target-injective at the tagged rank.

### Theorem 9.1 (diffuse independent choices leave \(e^{-1}\) holes)

The expected number \(M\) of uncovered targets satisfies

\[
 \boxed{
 \mathbb EM
 \ge N_q\exp\left[-{S\over N_q(1-\eta)}\right].}
\tag{9.2}
\]

Consequently, if \(q=o(\sqrt m)\), \(S/W\le1+o(1)\), and \(\eta=o(1)\),
then

\[
                              \boxed{\mathbb EM\ge(e^{-1}-o(1))W.}
\tag{9.3}
\]

#### Proof

Independence gives

\[
 \Pr(T\text{ is uncovered})=\prod_C(1-p_{C,T}).
\tag{9.4}
\]

For \(0\le p\le\eta<1\),

\[
                         1-p\ge\exp\left[-{p\over1-\eta}\right].
\tag{9.5}
\]

Thus the summand for \(T\) is at least
\(\exp[-\sum_Cp_{C,T}/(1-\eta)]\).  Convexity and
\(\sum_{C,T}p_{C,T}=S\) prove (9.2).  Finally
\(W/N_q=1+o(1)\) for \(q=o(\sqrt m)\), giving (9.3). \(\square\)

The same theorem gives a fixed positive obstruction at every fixed
Gaussian depth.  If \(q=\lfloor A\sqrt m\rfloor\), \(A\ge0\) is fixed,
\(S/W\to1\), and \(\eta=o(1)\), then the factorial product gives
\(W/N_q\to e^{A^2}\), and hence

\[
 \liminf {\mathbb EM\over N_q}\ge e^{-e^{A^2}},
 \qquad
 \liminf {\mathbb EM\over W}\ge e^{-A^2-e^{A^2}}>0.
\]

Thus mutually independent cell choices fail not only below
\(40\log m\), but at every fixed Gaussian coordinate as well.

For the complete affine conjugate menu on a \(Q_r\)-cell, at a depth in
its return-free target-injective range,

\[
                              \eta={2^q\over\binom rq}.
\tag{9.6}
\]

This tends to zero throughout the old short-depth interval when
\(r\) is polynomially larger than \(q\).  Therefore ordinary independent,
cellwise choices cannot remove the \(q<40\log m\) cutoff.  Pairwise
independence or zero cross-cell covariance alone is not covered by
Theorem 9.1; Section 10 separately shows that it cannot meet the required
balanced-floor conclusion.

Separate lower and upper tables also fail.  Near-perfect coverage on both
shores requires \(W-o(W)\) transition representatives to occur in both
tables, by (7.6).  If the tables are independent and every physical edge
has selection probability at most \(\eta=o(1)\) on each side, their
expected common representatives are at most

\[
                       \sum_ep_e^-p_e^+
                       \le\eta\sum_ep_e^-=o(W).
\tag{9.7}
\]

Thus the two signs must be coupled at the literal transition level.

Even a common Latin seed does not close this without a physical
intersection theorem.  Let \(z\) be uniform on a finite seed set
\(\Lambda\), and let

\[
 E_{i,T}^{q,\varepsilon}
 =\{z:\text{block }i\text{ emits }T
          \text{ at }(q,\varepsilon)\}.
\tag{9.8}
\]

Then the average number of holes is exactly

\[
 \sum_T\left(1-\mu\left(\bigcup_iE_{i,T}^{q,\varepsilon}\right)\right),
 \qquad \mu(E)={|E|\over|\Lambda|},
\tag{9.9}
\]

and the average duplicate excess is

\[
 \sum_T\left[
   \sum_i\mu(E_{i,T}^{q,\varepsilon})
   -\mu\left(\bigcup_iE_{i,T}^{q,\varepsilon}\right)
 \right]
 =S-N_q+\mathbb EM_q^\varepsilon.
\tag{9.10}
\]

A Latin condition fixes the individual measures in (9.8) but imposes no
bound on their intersections: equally Latin pullbacks can align the event
sets or make them disjoint.  At shallow load, near coverage is equivalent
to these rare event sets being an almost partition for almost every
literal target.  Proving that property for one common seed at every depth
and both signs is the missing full-profile difference-family theorem.
Separate seeds for different \(q\)'s do not define one successor factor.

## 10. Exact shallow floor-covariance demand

Let the retained owner mass be

\[
                              S=W-L,
\tag{10.1}
\]

and at depth \(q\) write

\[
 {S\over N_q}=c_q+\theta_q,qquad
 c_q=\left\lfloor{S\over N_q}\right\rfloor,qquad
 0\le\theta_q<1.
\tag{10.2}
\]

For a random integral common factor choice, let \(Z_T\) be the target
load at one fixed sign and depth, and define

\[
                        Q_q=\sum_T(Z_T-c_q)(Z_T-c_q-1).
\tag{10.3}
\]

### Lemma 10.1 (bias--variance--floor identity)

\[
 \boxed{
 \mathbb EQ_q
  =\sum_T\operatorname {Var}Z_T
   +\left\|\mathbb EZ-{S\over N_q}{\bf1}\right\|_2^2
   -N_q\theta_q(1-\theta_q).}
\tag{10.4}
\]

#### Proof

Expand each quadratic around the common mean \(S/N_q\), use
\(\sum_T\mathbb EZ_T=S\), and note that

\[
 \left({S\over N_q}-c_q\right)
 \left({S\over N_q}-c_q-1\right)
 =-\theta_q(1-\theta_q).
\tag{10.5}
\]

The cross term vanishes after summation. \(\square\)

At shallow depth the available integer reserve is tiny.  Since

\[
 {W\over N_q}=1+O\left({q^2+1\over m}\right)
                 \qquad(q=o(\sqrt m)),
\tag{10.6}
\]

one has

\[
                         N_q\theta_q(1-\theta_q)
                         =O\left(L+{W(q^2+1)\over m}\right).
\tag{10.7}
\]

Indeed, \(0\le S\le W\) and (10.6) imply \(c_q\in\{0,1\}\) for all
large \(m\).  If \(S/N_q\) lies above one then
\(\theta_q=S/N_q-1\); if it lies below one then
\(1-\theta_q=1-S/N_q\).  In either case
\(N_q\theta_q(1-\theta_q)\le |S-N_q|\), and (10.6) plus
\(S=W-L\) gives (10.7).

Put

\[
                              Q_0=\lceil40\log m\rceil.
\tag{10.8}
\]

If \(Q_0\le H\) and \(HL=o(W)\), then

\[
 \sum_{\varepsilon\in\{-,+\}}
 \sum_{q\le Q_0}N_q\theta_q(1-\theta_q)
 =O\left(Q_0L+{WQ_0^3\over m}\right)=o(W).
\tag{10.9}
\]

Now write the contribution of cell \(C\) as \(Y_{C,T}\), so

\[
                              Z_T=\sum_CY_{C,T}.
\tag{10.10}
\]

Then

\[
\begin{aligned}
 \sum_T\operatorname {Var}Z_T
 ={}&\sum_{C,T}\operatorname {Var}Y_{C,T}\\
 &+\sum_{C\ne C'}\sum_T
       \operatorname {Cov}(Y_{C,T},Y_{C',T}).
\end{aligned}
\tag{10.11}
\]

If every cell menu is target-injective and diffuse with maximum marginal
\(\eta=o(1)\), then

\[
 \sum_{C,T}\operatorname {Var}Y_{C,T}
 =\sum_{C,T}p_{C,T}(1-p_{C,T})
 \ge(1-\eta)S=(1-o(1))W
\tag{10.12}
\]

at each tagged row.  Combining (10.4), (10.9), and (10.11) proves the
necessary aggregate law

\[
 \boxed{
 \begin{aligned}
 &\sum_{\varepsilon\in\{-,+\}}\sum_{q\le Q_0}
   \sum_{C\ne C'}\sum_T
       \operatorname {Cov}(Y_{C,q,\varepsilon,T},
                           Y_{C',q,\varepsilon,T})\\
 &\qquad =-
 \sum_{\varepsilon\in\{-,+\}}\sum_{q\le Q_0}
   \sum_{C,T}\operatorname {Var}(Y_{C,q,\varepsilon,T})
 +o(W)
 \end{aligned}}
\tag{10.13}
\]

for every probabilistic construction whose expected total floor energy is
\(o(W)\) and whose aggregate squared one-point bias
\[
 \sum_{\varepsilon,q,T}
 \left(\mathbb EZ_{q,\varepsilon,T}-{S\over N_q}\right)^2
\]
is \(o(W)\).  It must cancel essentially
the whole cell diagonal, not a fixed positive fraction of it.

There is a packet-local Fourier form of the same obstruction.  On a
\(Q_r\)-packet of frame \(a\), let \(A_P\subseteq G/\langle a\rangle\)
be its active quotient-label set.  At depth one

\[
                              K_{P,1}=\mathbf1_{A_P}.
\tag{10.14}
\]

If the quotient has size \(m\), Parseval gives the exact nonconstant
energy

\[
 \sum_{\chi\ne1}
  \left|\sum_{v\in A_P}\chi(v)\right|^2
  =m|A_P|-|A_P|^2.
\tag{10.15}
\]

For \(|A_P|=m/4\), this is \(3m^2/16\).  An affine automorphism of the
quotient only permutes these characters and preserves (10.15).  A
lower-rank compatible hash can discard some modes, but is then blind to
their energy; balancing its bins does not cancel that energy.  Physical
cancellation requires signed inner products between different cells,
exactly as in (10.13).

## 11. Audited boundary

The following statements are proved.

* The exact all-depth configuration dual is (1.3), and owner leave changes
  a witness by at most \(2HL\).
* A single joint globally frame-compatible incidence hash is either an
  affine copy of \(\sigma\) or forces the sharp fixed-atlas leave (2.7).
* The complete compatible scalar row space has dimension (3.2), while a
  central-rank literal separator needs rank at least \(2m-2\).
* The frame-dependent hashes (4.6) are exact cell invariants with ranks
  (4.9)--(4.10) and exponentially balanced atomic parities.
* The hash slabs (5.2) admit exact common-owner perfect-matching option
  atlases, and the rainbow refinement has the uniform owner-leave bound
  (5.6) for every option vector.
* Every depth-one lower and upper target has a provider; the paired-colour
  Hall deficiency is \(o(W)\).
* Subject to the stated standard fixed-rank fractional-nibble theorem, the
  literal endpoint packing in Theorem 8.1 exists.  The only concentration
  input elsewhere is the explicitly identified standard Azuma inequality.
* Diffuse independent cell choices have the linear miss lower bound (9.2)
  at every fixed Gaussian depth, and a successful shallow rounding must
  obey the full negative covariance identity (10.13).

The fixed-atlas rigidity theorem and its constants were independently
audited.  The depth-one degree census, Hall-deficiency proof, hypergraph
degrees, codegrees, and fractional-nibble reduction were audited
separately.  The latter audit specifically confirms that iterative pruning
would have been unjustified; the fractional matching argument in Section 8
is the corrected proof.

The following statements are not proved.

* No selection of the frame-dependent hashes is shown to satisfy the
  configuration cuts (1.3).
* No Latin/permutation arrangement of the hash-slab options is shown to
  have the negative covariance (10.13).
* The partial depth-one router is not completed to status-cell cycle
  factors, has no \(o(W/H)\) quantitative leave, and has no component-count
  bound.
* No literal simultaneous coverage theorem is proved for any
  \(2\le q\le H\).
* The old \(q\ge40\log m\) hash-bin saturation and the present \(q=1\)
  endpoint packing are not supplied by one common successor factor.
* `CPM`, MWB, and \(\nu(k)=(1+o(1))W(k)\) remain unproved.

Thus the proposed extension by more globally compatible XOR hashes is
rigorously closed: it either adds no literal information or destroys the
owner-leave scale.  A frame-dependent orthogonal library and an exact
common-owner option atlas survive, and depth one is now reduced below Hall
capacity to cyclic completion.  The decisive open object is a genuinely
correlated, full-configuration physical router across status cells; it
cannot be replaced by independent hashes, separate lower/upper tables, or
Fourier balance of address bins.
