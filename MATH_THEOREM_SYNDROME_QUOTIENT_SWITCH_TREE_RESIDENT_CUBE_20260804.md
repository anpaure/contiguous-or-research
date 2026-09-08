# Syndrome-quotient switch trees give explicit resident cube Hamilton cycles

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical construction.  It gives a
structured long-run Hamilton cycle in a Boolean cube and hence in every
pair-cell Johnson cube above an explicit dimension threshold.  It does not
select one compatible pair cell for every middle owner and makes no palette
or compiler claim.

## 1. Statement

Write `Q_m` for the `m`-cube.  A cyclic transition word is **D-resident**
when two occurrences of the same coordinate direction have cyclic distance
at least `D`.

### Theorem 1.1

Let `D>=1`, let `h=2^s` be a power of two with

\[
                         h\ge 4D,                  \tag{1.1}
\]

and let `m>=h`.  Then `Q_m` has a `D`-resident Hamilton cycle.

The construction is explicit.  It starts from a vertex resolution into
isometric `2h`-cycles, identifies a basis of the component quotient by
literal square switches whose two active directions are at cyclic distance
at least `D`, and applies those switches along a Hamilton path of the
quotient cube.

Consequently, if `h(D)` is the least power of two at least `4D`, then

\[
             h(D)<8D,                               \tag{1.2}
\]

and every cube of dimension at least `h(D)` has such a structured resident
Hamilton cycle.

## 2. A syndrome resolution into isometric cycles

Put `U=F_2^s` and choose a binary reflected Gray ordering

\[
              u_0=0,u_1,\ldots,u_{h-1}              \tag{2.1}
\]

of all elements of `U`.  Let `b_1,...,b_s` be the standard basis.  Thus

\[
 u_i+u_{i-1}=b_{1+\nu_2(i)}
 \qquad(1\le i<h).                                  \tag{2.2}
\]

Adjoin one new syndrome direction `v` and put

\[
                    \Sigma=U\oplus\langle v\rangle.
\]

Define a linear map `phi:F_2^h->Sigma` on coordinate vectors by

\[
 \phi(e_i)=u_i+u_{i-1}\quad(1\le i<h),
 \qquad
 \phi(e_h)=v+u_{h-1}.                               \tag{2.3}
\]

Let `C` be the standard isometric cycle with transition word

\[
                  1,2,\ldots,h,1,2,\ldots,h.        \tag{2.4}
\]

If `p_i=e_1+...+e_i`, its vertex set is

\[
 P=\{p_i:0\le i<h\}\mathbin{\dot\cup}
   \{{\bf1}+p_i:0\le i<h\}.                       \tag{2.5}
\]

Telescoping (2.3) gives

\[
 \phi(p_i)=u_i,\qquad \phi({\bf1})=v.              \tag{2.6}
\]

Hence `phi` maps `P` bijectively onto `Sigma`.  If

\[
                         K=\ker\phi,                \tag{2.7}
\]

the cycles

\[
                         C+k\quad(k\in K)           \tag{2.8}
\]

are vertex-disjoint and partition `Q_h`.

Every cycle in (2.8) is `h`-resident: each direction occurs twice, at
antipodal transition positions.

## 3. A safe weight-two basis of the quotient

For `1<=j<=s`, let

\[
 I_j=\{i:1\le i<h,\ \phi(e_i)=b_j\}.                \tag{3.1}
\]

Equation (2.2) says that `I_j` consists of `c_j=h/2^j` equally spaced
positions on the cyclic set of `h` transition positions.  The last column
`phi(e_h)` has a nonzero `v`-coordinate and is in no `I_j`.

The kernel has the exact direct-sum description

\[
 K=\bigoplus_{j=1}^s
   \left\{x\in\mathbb F_2^{I_j}:\sum_{i\in I_j}x_i=0\right\}.
                                                               \tag{3.2}
\]

Indeed, a kernel vector has zero `e_h` coefficient because of the
`v`-coordinate, and then has even parity in every `I_j` because the
`b_j` are independent.

For every `I_j` with `c_j>=2`, make a graph on its cyclic positions by
joining two positions whose cyclic coordinate distance is at least `h/4`.
This graph is connected.  For `c_j=2` its only edge has distance `h/2`.
For `c_j>=4`, the step

\[
                       c_j/2-1                         \tag{3.3}
\]

is coprime to the power of two `c_j` and gives one spanning cycle; its
coordinate distance is

\[
 (c_j/2-1)2^j=h/2-2^j\ge h/4.                       \tag{3.4}
\]

Choose a spanning tree in each of these graphs.  For every tree edge `pq`,
take

\[
                         \delta_{pq}=e_p+e_q.         \tag{3.5}
\]

The union `S_K` of these vectors is a basis of `K`, by (3.2).  Moreover,
every chosen pair obeys

\[
                \operatorname{dist}_{\mathbb Z_h}(p,q)
                \ge h/4\ge D.                       \tag{3.6}
\]

The constant `1/4` is sharp for this particular weight-two kernel-basis
method.  When `s>=2`, the class `I_(s-2)` has four equally spaced
positions.  If one requires distance strictly greater than `h/4`, its legal
pair graph consists of the two antipodal edges.  Those two differences span
only a two-dimensional subspace, whereas the even-parity subspace on four
positions has dimension three.  Thus no basis of `K` made only of
equal-column weight-two differences can improve (3.6) beyond `h/4`.

### Lemma 3.1 (the active square switch)

Let `delta=e_p+e_q` belong to `S_K`.  For every `k in K`, corresponding
`q`-edges of `C+k` and `C+k+delta` are opposite sides of a literal
`p,q` square.  Deleting the two `q`-edges and inserting the two `p`-edges
merges the cycles.  Each new seam is `D`-resident.

#### Proof

If one `q`-edge is `x -> x+e_q`, the corresponding translated edge is

\[
 x+e_p+e_q\longrightarrow x+e_p.
\]

Replace them by

\[
 x\longrightarrow x+e_p,
 \qquad
 x+e_p+e_q\longrightarrow x+e_q.                   \tag{3.7}
\]

This is the directed two-cycle switch.  Around either seam the old cyclic
transition word at `q` is unchanged except that `q` is replaced by `p`.
By (3.6), `p` does not occur in the `(D-1)`-collar of `q`.  The two old
collars have the same orientation.  Their union is the length-`2D-2`
punctured interval around `q` in the `h`-periodic permutation word.  Since
`2D-2<h`, no other direction occurs twice in this union.  The deleted
direction `q` has its next retained occurrence at distance `h`, and the new
direction `p` has no collar occurrence.  Thus both seams are `D`-safe.
\(\square\)

## 4. The parity-twisted product resolution

The naive product of (2.8) over the remaining `m-h` coordinates has an
orientation defect: two cycles translated by one inactive direction have
parallel, not oppositely placed, cut edges, so the directed square switch
would require reversing one cycle and would duplicate its collar.

The following parity twist removes that defect.

Fix one active direction `q_0`.  Write an inactive assignment as
`z in F_2^(m-h)` and let

\[
                         \epsilon(z)=|z|\pmod2.      \tag{4.1}
\]

In the active subcube indexed by `z`, use the translated resolution

\[
       \mathcal R_z=
       \{C+k+z+\epsilon(z)e_{q_0}:k\in K\}.          \tag{4.2}
\]

Each `R_z` partitions its active subcube, so the cycles in all (4.2)
partition `Q_m`.

If `z` and `z+e_t` are adjacent inactive assignments, corresponding cycles
in their two resolutions differ by

\[
                         e_t+e_{q_0}.                \tag{4.3}
\]

Deleting corresponding `q_0`-edges and inserting the two `t`-edges is
therefore the same directed square switch as Lemma 3.1.  The cross direction
`t` is inactive inside both old cycles.  The remaining active collar
directions are distinct by the same `2D-2<h` argument as in Lemma 3.1, so
the two seams are `D`-safe.

Thus the component index set is the vector space

\[
                    \mathbb F_2^{m-h}\oplus K,       \tag{4.4}
\]

with literal safe switches for every member of the basis consisting of the
inactive coordinate vectors and `S_K`.

## 5. Port assignment and Hamiltonization

Take a Hamilton path of the basis cube (4.4).  Each path edge prescribes a
square switch and hence an active cut direction: `q_0` for an inactive
generator, and the chosen `q` in (3.5) for a kernel generator.

All old cycles are translates of the same equally oriented word (2.4).
Hence the two antipodal occurrences of every possible cut direction carry
one common occurrence-bit gauge.  A square switch uses the same occurrence
bit at its two endpoint components; no component-dependent reflection is
introduced.  This is the flat transport gauge missing from the naive
unshifted inactive product.

Every active direction occurs twice, at antipodal positions of the
`2h`-cycle.  Choose which occurrence is used by every quotient-path edge
recursively.  Once the occurrence for the preceding quotient edge is fixed,
the two occurrences available for the next cut are antipodal, so one is at
cyclic distance at least `h/2` from the preceding port.  Choose that one.
Therefore every original component used by two switches has its two deleted
edges at cyclic distance at least

\[
                         h/2\ge D.                  \tag{5.1}
\]

The endpoint components use only one port.

Apply the switches along the quotient Hamilton path.  The switch graph on
the old cycles is a spanning path, hence every switch joins two different
current components and all switches leave one Hamilton cycle.  The port
choices make the two deleted old edges distinct at every internal quotient
vertex, so all switches may equivalently be applied simultaneously.

The switches are globally separated: every retained old segment between
new seams has at least `D-1` old transitions by (5.1), and every seam is
`D`-safe by Lemma 3.1 or by the inactive-direction argument after (4.3).
Consequently any transition interval of length less than `D` meets at most
one new seam.  Old residence or the corresponding seam certificate applies,
so the final Hamilton cycle is `D`-resident.  This proves Theorem 1.1.

## 6. Pair-cell consequence and scope

A dimension-`m` pair cell in `J(2r,r)` is an induced `m`-cube: toggling one
cube direction swaps the two physical coordinates of its singleton pair.
Different cube directions have disjoint physical supports.  Hence a
`D`-resident transition word in `Q_m` embeds as a physical `D`-resident
Johnson Hamilton cycle in the cell.

The construction therefore closes the local good-cell chronology whenever

\[
                         m\ge h(D)<8D.               \tag{6.1}
\]

It is stronger structurally than a bare long-run existence theorem: the
cycle is obtained from isometric pieces by one explicit, globally separated
switch tree.

It does **not** prove that overlapping good cells from several coordinate
pairings admit one exact owner partition or one collar-compatible macro
selector.  Small cells in a fixed pairing are not repaired here.  Upper
palette, arbitrary-width upper witnesses, lower compilation, and component
router data are also outside the theorem.

The exact residence frontier after this construction is therefore global:

\[
 \boxed{\text{select one compatible family of these good-cell chronologies
 and preserve its switch-tree ports through the owner factor.}}
\]
