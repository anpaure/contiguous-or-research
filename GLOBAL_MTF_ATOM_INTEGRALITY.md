# Integrality for long-run MTF atoms: the OR-level target

## 1. The packing requirement was too strong

`GLOBAL_LONG_RUN_MTF_ATOMS.md` asked for atoms whose symmetric chains are
pairwise disjoint across the entire central band.  That would produce an
almost-SCD, but an OR array does not need an SCD.  It only needs every mask
to occur at least once.  Prefix chains belonging to different MTF paths may
overlap arbitrarily.

Let \(\mathcal A_1,\ldots,\mathcal A_p\) be genuine MTF atoms.  Atom \(j\)
has \(H_j\) states and initial state size at most \(s_j\).  Let
\(V_r\subseteq\binom{[k]}r\) be the set of distinct rank-\(r\) masks exposed
by all of their prefix chains, and put

\[
 Q=\sum_{r=1}^{k}\left(\binom kr-|V_r|\right).      \tag{1.1}
\]

### Theorem 1.1 (rank-defect accounting)

Without any disjointness assumption between different atoms,

\[
 \boxed{\quad
 \nu(k)\le \sum_{j=1}^p(H_j-1+s_j)+Q.
 \quad}                                             \tag{1.2}
\]

For radius-\(d_j\) long-run atoms, \(s_j\le2d_j+2\), and hence

\[
 \nu(2m)\le N+\sum_j(2d_j+1)+Q,
 \qquad N=\sum_jH_j.                                \tag{1.3}
\]

#### Proof

Initialize the prescribed first state of every atom by updating its blocks
in reverse order, then follow its \(H_j-1\) internal MTF updates.  Every set
in \(V_r\) is now a suffix OR at one of those endpoints.  Append each of the
\(Q\) missing masks literally.  Previously created witnesses are unchanged.
\(\square\)

Thus the correct target is not an integral atom packing.  It is a family
with

\[
 N=W+o(W),\qquad \sum_jd_j=o(W),\qquad Q=o(W).       \tag{1.4}
\]

In particular:

* middle sets may repeat \(o(W)\) times;
* nonmiddle rows need only be covered, not packed; and
* a different subfamily of states may supply each rank.

## 2. Exact orbit counts for one symmetric chain

Put \(n=2m\).  An oriented radius-\(d\) saturated symmetric chain is encoded
uniquely by

\[
 (L;z_1,\ldots,z_{2d};R),                           \tag{2.1}
\]

where \(|L|=|R|=m-d\), the three displayed parts partition \([2m]\), and
the chain is

\[
 L\subset L+z_1\subset\cdots\subset L+z_1+cdots+z_{2d}.
\]

There are exactly

\[
 C_d=\frac{(2m)!}{(m-d)!^2}                         \tag{2.2}
\]

such chains.

### Theorem 2.1 (chain degrees and codegrees)

Fix \(-d\le u\le d\).  A set \(S\) of rank \(m+u\) belongs to exactly

\[
 D_{d,u}=\frac{(m+u)!(m-u)!}{(m-d)!^2}              \tag{2.3}
\]

oriented radius-\(d\) chains.

If \(u<v\), \(|S|=m+u\), \(|T|=m+v\), then the number containing both is
zero unless \(S\subset T\).  In the comparable case it is

\[
 D_{d;u,v}
 =\frac{(m+u)!(v-u)!(m-v)!}{(m-d)!^2}.              \tag{2.4}
\]

Consequently

\[
 \frac{D_{d;u,v}}{D_{d,u}}
 =\frac1{\binom{m-u}{v-u}}.                         \tag{2.5}
\]

Two distinct sets of the same rank have codegree zero.

#### Proof

For (2.3), choose which \(m-d\) elements of \(S\) form \(L\), order the
remaining \(d+u\) elements of \(S\), and then choose and order the remaining
\(d-u\) chain increments from \([2m]\setminus S\).  This gives

\[
 \frac{(m+u)!}{(m-d)!}\frac{(m-u)!}{(m-d)!}.
\]

For (2.4), the elements of \(S-L\), \(T-S\), and the later increments must
occur in three consecutive portions of the increment word.  Their internal
orders are arbitrary, giving the displayed three factorials.  A chain has
one member at every supported rank, proving the remaining assertions.
\(\square\)

The \(\Theta(1/m)\) adjacent-rank codegree is therefore intrinsic to every
symmetric-chain formulation.  It is not caused by the long-run bundling.

## 3. Pascal-strip geometry inside one atom

Use a pair-orientation Gray-code block whose transition directions are
distinct throughout the block and its two radius-\(h\) halos.  Let

\[
 A_t^u
\]

denote the rank-\((m+u)\) member of the radius-\(h\) chain centered at the
\(t\)-th middle state, where \(-h\le u\le h\) and
\(0\le t<H\).

The pair states along the transition order have a simple form:

* for \(u=-q<0\), they are `old orientation / q empty pairs / new
  orientation`;
* for \(u=q>0\), they are `old orientation / q full pairs / new
  orientation`.

This gives an exact two-dimensional strip.

### Theorem 3.1 (Pascal-strip order)

For \(u<v\),

\[
 \boxed{\quad
 A_t^u\subset A_s^v
 \quad\Longleftrightarrow\quad
 0\le s-t\le v-u.
 \quad}                                             \tag{3.1}
\]

For equal ranks,

\[
 |A_t^u\setminus A_s^u|=|t-s|.                     \tag{3.2}
\]

whenever both starts lie in the block.

#### Proof

Moving from start \(t\) to \(t+1\) shifts the orientation frontier across
one previously unused pair direction.  In the same rank this deletes one
member and inserts one member, and distinct directions make these changes
accumulate without cancellation, proving (3.2).

Between two consecutive ranks every set has precisely two upper neighbours
inside the strip:

\[
 A_t^u\subset A_t^{u+1},\qquad
 A_t^u\subset A_{t+1}^{u+1}.                        \tag{3.3}
\]

The pair-state word shows that no other start can be comparable: outside
these two positions one pair has opposite singleton orientations and is
neither empty below nor full above.  Iterating (3.3) gives the forward
implication in (3.1), and the same mismatched-pair argument proves the
converse. \(\square\)

After the change of coordinates

\[
 (t,u)\longmapsto(t,t-u),
\]

equation (3.1) is ordinary product order in two coordinates.  The atom is
therefore literally a finite Pascal strip, not an unstructured large
hyperedge.

## 4. Exact codegrees of the full coordinate orbit

Fix one length-\(H\) Pascal-strip atom and take all its images under
\(S_{2m}\), counting group elements first; passing to distinct images divides
all degrees and codegrees by the same stabilizer.

At rank \(r=m+u\), the atom row is an \(H\)-vertex geodesic Johnson path.
For two fixed rank-\(r\) sets with

\[
 a=|S\setminus T|=|T\setminus S|,
\]

Theorem 3.1 gives the exact normalized codegree

\[
 \boxed{
 \frac{\deg(S,T)}{\deg(S)}
 =
 \begin{cases}
 \displaystyle
 \frac{2(H-a)}{H\binom{m+u}{a}\binom{m-u}{a}},
       &1\le a<H,\\[1.2ex]
 0,&a\ge H.
 \end{cases}}                                      \tag{4.1}
\]

In particular, uniformly for \(|u|=o(m)\),

\[
 \frac{\Delta_2^{\rm same\ rank}}D
 =\frac{2(H-1)}{H(m+u)(m-u)}
 =(2+o(1))m^{-2}.                                   \tag{4.2}
\]

For comparable sets \(S\subset T\) at signed depths \(u<v\), put
\(\ell=v-u\).  The number of comparable ordered position pairs in the base
atom is

\[
 M_\ell=\sum_{j=0}^{\ell}(H-j)
       =H(\ell+1)-\binom{\ell+1}{2}.                \tag{4.3}
\]

Consequently

\[
 \boxed{
 \frac{\deg(S,T)}{\deg(S)}
 =\frac{M_\ell}{H\binom{m-u}{\ell}}.
 }                                                   \tag{4.4}
\]

For adjacent ranks this is \((2+o(1))/m\).  Equations (4.2) and (4.4)
separate the two scales exactly:

* within one rank, atoms are extremely pseudorandom, with codegree
  \(\Theta(m^{-2})\);
* between adjacent ranks, their intended chain structure creates
  \(\Theta(m^{-1})\) clustering.

There is also an exact formula for every two-set relation type.  Assume
\(u<v\), put \(\ell=v-u\), and put

\[
 a=|S\setminus T|,
 \qquad |T\setminus S|=a+\ell .                    \tag{4.5}
\]

In the Pascal strip, if the two starts differ by \(\delta=s-t\), then

\[
 a=(-\delta)_+ +(\delta-\ell)_+ .                 \tag{4.6}
\]

Consequently the number of ordered base-position pairs of type
\((\ell,a)\) is

\[
 P_{\ell,0}=H(\ell+1)-\binom{\ell+1}{2},
 \qquad
 P_{\ell,a}=(H-a)_+ +(H-\ell-a)_+\quad(a>0),       \tag{4.7}
\]

and the full-orbit normalized codegree is

\[
 \boxed{
 \frac{\deg(S,T)}{\deg(S)}
 =\frac{P_{\ell,a}}
 {H\binom{m+u}{a}\binom{m-u}{a+\ell}} .}          \tag{4.8}
\]

Thus the only pair scale as large as \(m^{-1}\) is the intended adjacent
inclusion relation.  A noncomparable pair in ranks differing by \(\ell\)
has ratio \(O(m^{-\ell-2})\).

### 4.1 Exact nested higher codegrees

Let

\[
 S_1\subset S_2\subset\cdots\subset S_j,
 \qquad |S_i|=m+u_i,
 \qquad \ell_i=u_{i+1}-u_i>0,                     \tag{4.9}
\]

and suppose \(L=\sum_i\ell_i<H\).  A base realization is specified by
shifts \(0\leq\delta_i\leq\ell_i\).  Summing the available translations
gives

\[
 P(\ell_1,\ldots,\ell_{j-1})
 =\prod_{i=1}^{j-1}(\ell_i+1)
   \left(H-\frac L2\right).                       \tag{4.10}
\]

Conditioned on \(S_1\), the number of ambient nested tuples of this type is

\[
 \frac{(m-u_1)!}
 {(m-u_j)!\prod_{i=1}^{j-1}\ell_i!}.              \tag{4.11}
\]

Therefore

\[
 \boxed{
 \frac{\deg(S_1,\ldots,S_j)}{\deg(S_1)}
 =\frac{\prod_i(\ell_i+1)(H-L/2)}{H}
   \frac{(m-u_j)!\prod_i\ell_i!}{(m-u_1)!}.}      \tag{4.12}
\]

For consecutive ranks this is

\[
 \frac{2^{j-1}(H-(j-1)/2)}
 {H(m-u_1)_{j-1}}
 =(1+o(1))(2/m)^{j-1}.                            \tag{4.13}
\]

By contrast, \(j\) consecutive vertices in one rank require one deletion
and one insertion at each step and have normalized codegree
\(\Theta(m^{-2(j-1)})\).  The vertical nested hierarchy is the largest
low-order codegree hierarchy.

### 4.2 The high-order rectangle obstruction

The low-order decay does **not** make the complete Pascal-strip atom
suitable for a full-codegree nibble.  An \(a\)-by-\(b\) rectangle of strip
positions has \(ab\) vertices but is generated from one corner by only

\[
 2(a-1)+(b-1)=2a+b-3                              \tag{4.14}
\]

changing coordinates: a horizontal step is one deletion and one insertion,
whereas a vertical step is one insertion.  Its orbit codegree consequently
has polynomial exponent \(2a+b-3\), not \(ab-1\).  Taking
\((ab-1)\)-st roots produces the scale

\[
 m^{-\,(2a+b-3)/(ab-1)},                          \tag{4.15}
\]

which approaches one when both side lengths grow.

There is a clean rigorous version using the whole edge.  A full atom has

\[
 R=H(2h+1)                                        \tag{4.16}
\]

vertices, but after one vertex is fixed all other vertices differ from it
on only \(O(H+h)\) active coordinates.  Hence its degree in the simple
coordinate orbit satisfies

\[
 D\leq R(2m)^{O(H+h)}.                             \tag{4.17}
\]

The full edge has \(R\)-codegree one, so the Gould--Kelly full-codegree
parameter is bounded by

\[
 B\leq D^{1/(R-1)}
 \leq\exp\!\left(O\!\left(\frac{\log m}{h}
                         +\frac{\log m}{H}\right)\right).     \tag{4.18}
\]

For \(h\gg\log m\) and \(H\gg h\), this is \(1+o(1)\).  Thus the
obstruction is not merely that available theorems fix the uniformity: the
complete two-dimensional atom has genuine high-order clustering, and the
strongest full-codegree parameter correctly detects it.  A successful
rounding argument must sparsify the certificate inside an atom, proceed
rank by rank, or permit overlaps instead of matching complete atoms.

## 5. Generic matching theorems do not yet round a growing row

Let \(h=o(m)\), and choose

\[
 h\ll H=o(m).                                       \tag{5.1}
\]

For instance, when \(h=\Theta(\sqrt{m\log m})\), one may take

\[
 H=m/\log m.                                        \tag{5.2}
\]

At any fixed supported rank, the full-orbit row hypergraph is regular,
\(H\)-uniform, and by (4.2) satisfies

\[
 \frac{\Delta_2}{D}=O(m^{-2})
 =o\!\left(\frac1{H\log |V|}\right),               \tag{5.3}
\]

because \(\log|V|=\Theta(m)\) and \(H=o(m)\).

Equation (5.3) looks strong, but it does **not** imply a near-perfect
matching when \(H\) grows.  The earlier invocation of Grable's theorem here
was invalid.

The relevant quantitative leftover has the shape

\[
 |V|\left(\frac{H\Delta_2\log|V|}{D}\right)^{
             1/(2H-1+o(H))}.                       \tag{5.4}
\]

For \(H=m/\log m\), the base in parentheses is
\(\Theta(1/\log m)\), but the exponent is
\(\Theta(\log m/m)\).  The displayed factor therefore tends to one, not
zero.  The same issue persists throughout the useful growing range
\(h\ll H\le m\).

The 2025 Gould--Kelly full-codegree nibble cannot presently be quoted
either.  Its theorem uses the fixed-uniformity hierarchy

\[
 1/D\ll1/A\ll\gamma\ll1/H,
\]

and gives leftover \(|V|B^{-1+\gamma}\log^A D\).  It supplies no uniform
dependence for \(H=H(m)\to\infty\).  For a single row, the pair bottleneck
already gives at best \(B=\Theta(m)\); since \(\log D=\Theta(H\log m)\),
the written polylogarithmic loss is not controlled in this diagonal
regime.  For the complete all-rank atom the situation is decisively worse:
the high-order rectangle bound (4.18) gives \(B=1+o(1)\).

Vu's theorem and the theorem of Kang--K\"uhn--Methuku--Osthus also fix the
uniformity.  Formally substituting \(H\to\infty\) leaves an exponent of
order \(1/H\), and the latter theorem additionally requires a fixed power
gap \(D_2\leq D^{1-\gamma}\), which is absent here.

Thus even the following one-row assertion remains open by the audited
black boxes:

> For \(h\ll H\le m\), does the fixed-rank row orbit have a matching
> missing \(o(|V|)\) vertices?

The exact same-rank codegree (4.2) is strong evidence, but a proof must be
quantitative while the edge size grows.

## 6. Deep ranks cost only an \(o(W)\) reservoir

The OR-cover formulation allows a further unconditional reduction.  Fix

\[
 h=\lceil\sqrt{m\log m}\rceil,qquad
 H=m/\log m,qquad
 \delta=1/\log m.                                  \tag{6.1}
\]

Choose

\[
 M=\left\lceil\delta W/H\right\rceil              \tag{6.2}
\]

independent uniformly random radius-\(h\) atoms from the full coordinate
orbit.  Repetitions and overlaps are allowed: this is an auxiliary cover,
not the main middle packing.

### Lemma 6.1 (random deep-cover reservoir)

Let

\[
 q_0=\left\lceil\sqrt{8m\log\log m}\right\rceil.   \tag{6.3}
\]

There is a choice of the \(M\) atoms for which the total number of uncovered
masks in all ranks with

\[
 q_0\le |r-m|\le h
\]

is \(o(W)\).  The array length needed to traverse the reservoir atoms is
also \(o(W)\).

#### Proof

A fixed target at depth \(q\le h\) belongs to a uniformly random atom with
probability exactly \(H/N_q\), where

\[
 N_q=\binom{2m}{m-q}.
\]

Hence its miss probability is at most

\[
 \left(1-\frac H{N_q}\right)^M
 \le \exp\!\left(-\delta W/N_q\right).              \tag{6.4}
\]

For \(q=o(m)\), the elementary central-binomial product gives

\[
 \frac W{N_q}\ge\exp(q^2/(2m)).                    \tag{6.5}
\]

At \(q=q_0\), the right side is at least \((\log m)^4\), so the exponent
in (6.4) is at least \((\log m)^3\).  It only increases with \(q\).
Therefore the expected total number of misses is at most

\[
 2hW\exp(-(\log m)^3)=o(W).                        \tag{6.6}
\]

Some deterministic choice attains this bound.  Each atom costs at most
\(H+2h+1\) entries, so the reservoir length is

\[
 M(H+2h+1)
 =O(\delta W(1+h/H))=o(W).                         \tag{6.7}
\]

\(\square\)

This is a genuine bootstrap theorem: an asymptotically width-sized
construction only has to solve the simultaneous row problem through depth

\[
 \Theta(\sqrt{m\log\log m}),                       \tag{6.8}
\]

not through the \(\Theta(\sqrt{m\log m})\) depth required to make literal
tails negligible.  The deeper central ranks are supplied by a vanishing
length reservoir, and the outer tails are still appended literally.

## 7. The rotor graph on oriented chains

The exact composition problem also has a compact state-free form.  Encode a
radius-\(d\) oriented chain by (2.1).  Choose

\[
 x\in L,qquad y\in R.
\]

Its canonical MTF successor is

\[
\begin{aligned}
(L;z_1,\ldots,z_{2d};R)
\longmapsto
(&L-x+y;\\
 &x,z_1,\ldots,z_{2d-1};\\
 &R-y+z_{2d}).                                      \tag{7.1}
\end{aligned}
\]

### Lemma 7.1 (chain rotor)

The directed graph (7.1) is \((m-d)^2\)-regular in both directions, and
every one of its arcs is an exact one-entry MTF transition exposing the two
chains.

#### Proof

The forward choice is the ordered pair \((x,y)\in L\times R\).  To invert
(7.1), the new first increment determines \(x\); choose the old last
increment from the new residual set and choose the entering element from the
new minimum.  This again gives \((m-d)^2\) choices.  Formula (7.1) is exactly
the block calculation in Theorem 3.1 of
`GLOBAL_LONG_RUN_MTF_ATOMS.md`. \(\square\)

### Lemma 7.2 (cyclic orders are rigid rotor cycles)

Temporarily order the elements inside `L` and `R`, writing

\[
 W=(\ell_1,\ldots,\ell_a,
       z_1,\ldots,z_{2d},
       r_1,\ldots,r_a),\qquad a=m-d.                \tag{7.2}
\]

In (7.1) choose `x=ell_a` and `y=r_a`, and order the new blocks as

\[
\begin{aligned}
 L'&=(r_a,\ell_1,\ldots,\ell_{a-1}),\\
 Z'&=(\ell_a,z_1,\ldots,z_{2d-1}),\\
 R'&=(z_{2d},r_1,\ldots,r_{a-1}).
\end{aligned}                                      \tag{7.3}
\]

Then the complete coordinate word is rotated one place:

\[
                         W'=(w_{2m},w_1,\ldots,w_{2m-1}).
\tag{7.4}
\]

Consequently this rotor orbit has `2m` chain states, and at every rank
`m+u` its exposed sets are exactly the cyclic intervals of length `m+u` in
the cyclic coordinate order `W`.

#### Proof

Concatenating the three lines of (7.3) gives (7.4) term by term.  The
rank-`m+u` member consists of `L` and the first `d+u` entries of `Z`, hence
is the consecutive block of `m+u` positions beginning at the current cut.
Rotating through all cuts gives all cyclic intervals. \(\square\)

This identifies the two global formulations inside one graph.  A wreath is
a rigid cyclic rotor orbit; a vertically resolved wreath factor tiles rank
rows with such cycles; long-run atoms instead use flexible noncyclic rotor
paths.

Thus the remaining shallow-band theorem may be stated without ordered
partitions:

> Choose one oriented chain above almost every middle set, covering the
> shallow ranks with total defect \(o(W)\), so that the chosen chains have a
> rotor-graph path cover with total initialization cost \(o(W)\).

This is weaker than an SCD and weaker than an atom packing.

## 8. The exact remaining integrality target

Combine Theorem 1.1 and Lemma 6.1.  It is enough to prove:

> **Shallow simultaneous row-cover theorem.**  With
> \(q_0=\Theta(\sqrt{m\log\log m})\), choose
> \(W+o(W)\) centers arranged in long rotor/atom paths, such that the sum of
> the missing-mask counts over the ranks
> \(|r-m|\le q_0\) is \(o(W)\).

The exact orbit calculation shows why standard black boxes split here:

\[
 \text{same-rank codegree }\Theta(m^{-2}),
 \qquad
 \text{adjacent-rank codegree }\Theta(m^{-1}).
\]

Group-orbit design theorems with fixed block size do not directly apply,
because both \(H\) and \(q_0\) grow.  A successful proof must first obtain
uniform growing-row integrality and then couple the rows, or use the
Pascal-strip structure (3.1) in an outer-to-inner absorption which regards
the adjacent-rank correlations as prescribed chain links rather than as
harmful codegrees.

What is now rigorously removed from the problem is substantial:

* full atom disjointness is unnecessary;
* all sufficiently deep ranks cost only \(o(W)\) extra entries; and
* MTF composition is the explicit regular rotor (7.1).

The unresolved part is shallow growing-row integrality and its simultaneous
coupling.
