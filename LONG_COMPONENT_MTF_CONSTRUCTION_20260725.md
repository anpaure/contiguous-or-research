# Long residual-consuming MTF components at a growing depth

Date: 2026-07-25

## Status

This note does **not** prove the Gaussian-window portal--trace theorem and
does not prove the coefficient-one conjecture.  It proves a positive result
on exactly the side left open by the residual-depletion dichotomy.

There is a prescribed, nontrivially growing range

\[
 H\longrightarrow\infty,
 \qquad
 H=o\!\left(\frac{\log m}{\log\log m}\right)
 \tag{0.1}
\]

in which one can select residual-consuming canonical MTF components such
that

* the components contain all but \(o(W)\) middle owners;
* every component has length \(\omega(H)\);
* the number of components is \(o(W/H)\);
* their canonical rank-\((m+H)\) masks are globally distinct and miss only
  \(o(W)\) targets; and
* even completely independent exact-state initialization has portal excess
  \(o(W)\).

In fact these components give a literal word of length \(W+o(W)\) covering
the entire middle rank and the entire single upper rank \(m+H\).

Thus the depletion theorem's surviving positive case is real at a growing
depth.  The new ingredient is to match only the middle row and the one
deepest upper row of each strip.  Encoding all \(2H+1\) rows in the same
matching edge is unnecessary for this two-rank conclusion and increases the
uniformity by a factor \(H\).

Throughout,

\[
 n=2m,
 \qquad
 W=\binom{2m}{m},
 \qquad
 N_H=\binom{2m}{m+H}.
 \tag{0.2}
\]

No computation or search is used.

---

## 1. Cyclic strips and the projected two-row hypergraph

Choose disjoint sets \(C,D\subset[2m]\) with

\[
 |C|=|D|=m-\ell,
 \tag{1.1}
\]

and put

\[
 R=[2m]\setminus(C\cup D),
 \qquad |R|=2\ell.
\]

Give \(R\) an undirected cyclic order

\[
 \gamma=(z_0,z_1,\ldots,z_{2\ell-1}).
\]

For cyclic intervals \(I_\gamma(i,a)\), define

\[
 T_i=C\cup I_\gamma(i,\ell),
 \tag{1.2}
\]

and

\[
 U_i=C\cup I_\gamma(i-H,\ell+H),
 \qquad i\in\mathbb Z_{2\ell}.
 \tag{1.3}
\]

The \(T_i\)'s are a Johnson cycle in the middle layer, and the \(U_i\)'s
are the cyclic upper depth-\(H\) masks of that cycle.

Let \(\mathcal G^+_{m,H,\ell}\) be the simple hypergraph whose vertex set is
the disjoint union

\[
 V_0\sqcup V_H
 =\binom{[2m]}m\sqcup\binom{[2m]}{m+H},
 \tag{1.4}
\]

and whose edges are

\[
 E(C,D,\gamma)
 =\{T_i:i\in\mathbb Z_{2\ell}\}
  \sqcup
  \{U_i:i\in\mathbb Z_{2\ell}\}.
 \tag{1.5}
\]

Thus its uniformity is only

\[
 K=4\ell.
 \tag{1.6}
\]

The hypergraph is simple.  Indeed the intersection of the middle row is
\(C\), its union is \(C\cup R\), and the induced Johnson adjacencies recover
the cyclic order on \(R\) up to reversal.  Hence the middle row alone
recovers \((C,D,\gamma)\).

### Lemma 1.1 -- degrees

A rank-\((m+d)\) vertex has degree

\[
 D_d=
 \frac{(m+d)!(m-d)!}{2(m-\ell)!^2},
 \qquad d\in\{0,H\}.
 \tag{1.7}
\]

In particular, with \(D=D_H\),

\[
 \frac{D}{D_0}
 =\frac{(m+H)!(m-H)!}{m!^2}
 \le \exp\!\left(\frac{H^2}{m-H}\right),
 \tag{1.8}
\]

and, when \(\ell=o(m)\),

\[
 \log D=(2+o(1))\ell\log m.
 \tag{1.9}
\]

#### Proof

The usual strip count gives

\[
 |E(\mathcal G^+)|
 =\frac{(2m)!}{4\ell(m-\ell)!^2}.
\]

Every edge has \(2\ell\) vertices in each of its two parts.  Double
counting incidences in either transitive rank gives (1.7).  Formula (1.8)
is exact before the displayed upper bound; take logarithms and bound each
of the \(H\) factors by \(H/(m-H)\).  Formula (1.9) follows from the two
falling factorials of length \(\ell\).  \(\square\)

### Lemma 1.2 -- a uniform codegree bound

Assume

\[
 \ell-H\ge2,
 \qquad
 \ell<m.
 \tag{1.10}
\]

The maximum pair-codegree \(\Gamma\) satisfies

\[
 \boxed{
 \Gamma\le \frac{2\ell D}{m-H}.}
 \tag{1.11}
\]

#### Proof

Fix a vertex \(X\) and a distinct second vertex \(Y\).  Under the
stabilizer of \(X\), the orbit of \(Y\) has size

\[
 \binom{|X|}{|X\setminus Y|}
 \binom{2m-|X|}{|Y\setminus X|}.
 \tag{1.12}
\]

Every nontrivial orbit relevant to the two selected ranks has size at least
\(m-H\).  The only possible nontrivial-looking orbit of size one is the
complement of a middle set.  It has codegree zero: all members of one strip
contain the nonempty common core \(C\), so two complementary middle sets do
not occur together.

For an orbit \(\mathcal O\), double count pairs \((E,Y')\) with
\(X,Y'\in E\) and \(Y'\in\mathcal O\).  Every edge through \(X\) contains
at most \(2\ell\) vertices in the rank of \(Y\).  Stabilizer symmetry then
gives

\[
 |\mathcal O|\deg(X,Y)\le2\ell\deg(X)\le2\ell D.
\]

This proves (1.11).  \(\square\)

The sharper bound \(\Gamma/D=O(1/m)\) is available for full strips, but is
not needed below.

---

## 2. A quantitative two-row matching

Put

\[
 L=\log m,
 \qquad
 \lambda=\log L,
 \qquad
 \ell=\left\lfloor\frac{L}{32\lambda}\right\rfloor.
 \tag{2.1}
\]

Let \(H\) be any integer function satisfying (0.1).  Then (1.10) holds for
all sufficiently large \(m\).

We use the same quantitative near-regular matching theorem already used in
the audited full-strip construction.  In the form needed here it says the
following.  A simple \(K\)-uniform hypergraph of maximum degree \(D\),
minimum degree at least

\[
 D-20(D^2C\log D)^{1/3},
\]

and maximum pair-codegree at most \(C\), has a matching leaving at most

\[
 O\!\left(
 K\left(\frac{C\log(1+C)}D\right)^{1/(K-1)}|V|
 \right)
 \tag{2.2}
\]

vertices, provided the standard hypotheses

\[
 K\le\tfrac12\log D,
 \qquad
 e^{2K}C\log D=o(D),
 \tag{2.3}
\]

and the displayed degree-error condition hold.

### Theorem 2.1 -- projected strip matching

For every \(H\) satisfying (0.1), the hypergraph
\(\mathcal G^+_{m,H,\ell}\) has a matching for which the total uncovered
vertex count \(U\) satisfies

\[
 \boxed{
 U\le W(\log m)^{-7+o(1)}=o(W).}
 \tag{2.4}
\]

#### Proof

Take

\[
 C_*=\left\lceil\frac{2\ell D}{m-H}\right\rceil.
 \tag{2.5}
\]

Lemma 1.2 gives \(\Gamma\le C_*\).  By (1.9),

\[
 \eta:=\frac{C_*\log(1+C_*)}{D}
 =O\!\left(\frac{\ell^2L}{m}\right),
 \tag{2.6}
\]

so

\[
 \log\eta=-L+O(\lambda).
 \tag{2.7}
\]

Since

\[
 K=4\ell=(1+o(1))\frac{L}{8\lambda},
\]

we obtain

\[
 \eta^{1/(K-1)}
 =L^{-8+o(1)}.
 \tag{2.8}
\]

The degree defect in (1.8) is \(O(H^2/m)\).  This is

\[
 o\!\left[
 \left(\frac{C_*\log D}{D}\right)^{1/3}
 \right],
 \tag{2.9}
\]

because \(H\le\ell\) eventually and all of \(H,\ell,L\) are
polylogarithmic while the two powers of \(m\) differ.  Thus the
near-regularity requirement holds.

Also

\[
 \frac K{\log D}=O(1/L)=o(1),
\]

and

\[
 \log\!\left(e^{2K}\frac{C_*\log D}{D}\right)
 \le -L+\frac{L}{4\lambda}+O(\lambda)
 =-(1-o(1))L.
 \tag{2.10}
\]

Hence (2.3) holds.  Substitution of (2.8) in (2.2), together with
\(|V|=W+N_H=O(W)\), gives

\[
 U=O\!\left(\frac L\lambda L^{-8+o(1)}W\right)
 =W L^{-7+o(1)}.
\]

This proves (2.4).  \(\square\)

If the matching has \(p\) strips, write

\[
 u_0=W-2\ell p,
 \qquad
 u_H^+=N_H-2\ell p.
 \tag{2.11}
\]

Then

\[
 u_0+u_H^+=U=o(W),
 \tag{2.12}
\]

and therefore

\[
 p=(1-o(1))\frac{W}{2\ell}.
 \tag{2.13}
\]

---

## 3. Exact delayed-deletion schedule and virtual closure

Cut the edge \(T_{2\ell-1}T_0\) in every selected middle cycle.  Along the
resulting path use

\[
 p_i=z_i,
 \qquad
 q_i=z_{i+\ell},
 \tag{3.1}
\]

with cyclic indices for terminal dummy departures.  Thus

\[
 \boxed{q_i=p_{i+\ell}.}
 \tag{3.2}
\]

Every positive coordinate run has cyclic length exactly \(\ell\), so the
path is \(H\)-legal because \(\ell>H\).

Initialize the upper queue by

\[
 \Theta_0=
 (\{z_{2\ell-1}\},\ldots,\{z_{2\ell-H}\},R_0),
 \tag{3.3}
\]

where

\[
 R_0=D\cup
 \{z_\ell,z_{\ell+1},\ldots,z_{2\ell-H-1}\}.
 \tag{3.4}
\]

The canonical recurrence prepends \(p_i\) and deletes \(q_i\).  Since
\(\ell>H\), no arrival deletes one of the last \(H\) departures.  Hence at
state \(i\) the first \(H\) upper singletons are

\[
 z_{i-1},z_{i-2},\ldots,z_{i-H}.
 \tag{3.5}
\]

Consequently the canonical deepest upper mask at state \(i\) is exactly

\[
 T_i\cup\{z_{i-1},\ldots,z_{i-H}\}
 =C\cup I_\gamma(i-H,\ell+H)
 =U_i.
 \tag{3.6}
\]

This proves three useful facts at once.

1. Cutting the middle cycle loses **none** of its \(2\ell\) cyclic upper
   depth-\(H\) masks.
2. All these masks are distinct within one component.
3. Because the strips form a matching in \(\mathcal G^+\), they are also
   distinct between different components.

The same schedule identifies the residual behavior exactly.  Every one of
the \(\ell-H\) active coordinates in (3.4) arrives during the path, while
no point of \(D\) ever arrives.  The terminal residual is therefore

\[
 R_{\rm end}=D,
 \qquad |D|=m-\ell<m-H.
 \tag{3.7}
\]

Thus **every selected component is residual-consuming**.  The construction
does not evade the depletion dichotomy by hiding in the fixed-residual
class; it realizes its surviving long-component alternative.

---

## 4. The long-component theorem

### Theorem 4.1 -- growing-depth long consuming components

Let \(H\) satisfy (0.1), and let \(\ell\) be (2.1).  For all sufficiently
large \(m\), there is a family of \(p\) canonical radius-\(H\) MTF path
components such that

\[
 \boxed{
 \begin{aligned}
 2\ell p&=W-o(W),\\
 p&=o(W/H),\\
 2\ell/H&\longrightarrow\infty,
 \end{aligned}}
 \tag{4.1}
\]

every component is residual-consuming, and their canonical deepest-upper
support has size

\[
 \boxed{
 |\mathcal S_H^+|=2\ell p=N_H-o(W).}
 \tag{4.2}
\]

Moreover their independently initialized portal excess is

\[
 \boxed{
 \mathfrak P_H=(2H+1)p=o(W).}
 \tag{4.3}
\]

#### Proof

Equations (4.1)--(4.2) follow from (2.11)--(2.13), (0.1), and
\(\ell\asymp L/\lambda\).  Residual consumption and exact upper support are
proved in Section 3.

The canonical word for one path of \(2\ell\) middle states has length

\[
 2\ell+2H+1.
\]

Concatenating independently initialized path words gives portal excess
\((2H+1)p\).  Since

\[
 \frac{(2H+1)p}{W}
 \le\frac{2H+1}{2\ell}=o(1),
\]

(4.3) follows.  \(\square\)

At this scale \(H=o(\sqrt m)\), so

\[
 N_H=(1-o(1))W.
 \tag{4.4}
\]

Thus the phrase "many distinct upper masks" in (4.2) means nearly the
whole rank, not merely a growing but negligible family.

### Corollary 4.2 -- a literal two-rank word

There is a nonzero contiguous-OR word of length

\[
 \boxed{W+o(W)}
 \tag{4.5}
\]

covering every mask in ranks \(m\) and \(m+H\).

#### Proof

Use the \(p\) canonical component words.  Append the \(u_0\) uncovered
middle masks and the \(u_H^+\) uncovered upper masks literally.  The total
length is

\[
 \begin{aligned}
 p(2\ell+2H+1)+u_0+u_H^+
 &=W+(2H+1)p+u_H^+\\
 &=W+o(W).
 \end{aligned}
\]

Every entry is nonempty.  Section 3 supplies the physical contiguous-OR
certificates for all selected upper masks.  \(\square\)

This corollary is deliberately only a two-rank theorem.  Matching one
deepest row does not control the cumulative defects at all intermediate
depths.

### Corollary 4.3 -- symmetric three-rank version

Under the same hypothesis (0.1), there is a nonzero contiguous-OR word of
length (W+o(W)) covering every mask in the three ranks

\[
 m-H,\qquad m,\qquad m+H.
 \tag{4.6}
\]

#### Proof

Replace the two-row hypergraph by the projection onto the three rows

\[
 C\cup I_\gamma(i+H,\ell-H),\qquad
 C\cup I_\gamma(i,\ell),\qquad
 C\cup I_\gamma(i-H,\ell+H).
 \tag{4.7}
\]

Its uniformity is \(K=6\ell\).  Choose instead

\[
 \ell=\left\lfloor\frac{L}{48\lambda}\right\rfloor.
 \tag{4.8}
\]

The degree and codegree proofs in Sections 1--2 are unchanged.  Now again

\[
 K=(1+o(1))\frac{L}{8\lambda},
\]

so the exponent in (2.8) remains (L^{-8+o(1)}), and the three-row
matching leaves \(o(W)\) masks in total.  Virtual cyclic closure exposes all
\(2\ell\) selected masks in both extreme rows.  Append the uncovered middle
and extreme-rank masks literally.  The selected component words have portal
excess at most

\[
 (2H+1)\frac{W}{2\ell}=o(W),
\]

which proves the claim.  \(\square\)

This still does not control any of the (2H-2) omitted intermediate ranks.

### Theorem 4.4 -- sparse-row interpolation

Let

\[
 \mathcal D_m\subseteq\{-H,-H+1,\ldots,H\},
 \qquad 0\in\mathcal D_m,
 \qquad r=|\mathcal D_m|.
 \tag{4.9}
\]

Take \(H=\max_{d\in\mathcal D_m}|d|\ge1\).

Suppose

\[
 \boxed{
 \frac{rH\log\log m}{\log m}\longrightarrow0.}
 \tag{4.10}
\]

Then there is a literal nonzero contiguous-OR word of length (W+o(W))
covering every mask in every selected rank

\[
 m+d,
 \qquad d\in\mathcal D_m.
 \tag{4.11}
\]

The word's selected middle owners lie on residual-consuming canonical
components of length \(\omega(H)\), and their number is \(o(W/H)\).

#### Proof

Project each strip onto the (r) row families

\[
 \{C\cup I_\gamma(i,\ell+d):i\in\mathbb Z_{2\ell}\},
 \qquad d\in\mathcal D_m,
 \tag{4.12}
\]

and take

\[
 \ell=\left\lfloor
 \frac{L}{16r\lambda}
 \right\rfloor.
 \tag{4.13}
\]

Condition (4.10) gives (H/\ell\to0), so all rows are legal and every
selected component is super-\(H\)-long and residual-consuming.  The
projected hypergraph is simple because it contains the middle row.  Its
uniformity is

\[
 K=2\ell r=(1+o(1))\frac{L}{8\lambda}.
 \tag{4.14}
\]

The degree and codegree calculations of Sections 1--2 apply verbatim, with
maximum degree (D_H).  In particular the normalized codegree parameter
still has logarithm (-L+O(\lambda)), and therefore its (1/(K-1)) power
is (L^{-8+o(1)}).  The matching residual is at most

\[
 O\!\left(KL^{-8+o(1)}rW\right)
 =O\!\left(rL^{-7+o(1)}W\right)
 =o(W),
 \tag{4.15}
\]

because (4.10) implies (r=o(L/\lambda)).  Thus the matching misses only
\(o(W)\) masks in total across all selected ranks.

Virtual cyclic closure exposes all (2\ell) matched labels in every
selected signed depth.  Append every unmatched selected-rank mask
literally.  The portal excess is at most

\[
 (2H+1)\frac{W}{2\ell}=o(W),
 \tag{4.16}
\]

and the middle row plus its unmatched literals contributes exactly (W)
entries before this portal and repair excess.  This proves (4.11).
Finally

\[
 p\le W/(2\ell)=o(W/H),
\]

and (2\ell/H\to\infty).  \(\square\)

The theorem explains the two established scales in one line.

* If all (2H+1) band rows are selected, then (r\asymp H) and (4.10)
  becomes
  \[
  H=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).
  \]
* If only a fixed number of rows is selected, then (4.10) becomes
  \[
  H=o\!\left(\frac{\log m}{\log\log m}\right).
  \]

So the new long-component theorem is not an isolated trick: it is the
sparse-row endpoint of the same projected-strip matching calculation.

---

## 5. Sharp comparison with the depletion lower bound

Let \(D_{\rm comp}=p\) denote the number of residual-consuming components.
The audited depletion theorem gives, for every ordering and every exact
bridge system,

\[
 \mathfrak P_H\ge2H+1+2H(p-1)=2Hp+1.
 \tag{5.1}
\]

Our independent-reset value is

\[
 (2H+1)p.
 \tag{5.2}
\]

Therefore

\[
 \frac{(2H+1)p}{2Hp+1}=1+O(1/H).
 \tag{5.3}
\]

So, for this system, independent initialization is already asymptotically
optimal among all exact-state portal orderings.  The gain comes from making
the consuming components long, not from finding unexpectedly cheap bridges
between depleted states.

The fixed-residual alternative cannot give the same support.  A
residual-preserving component has one constant deepest-upper mask.  Under
portal excess \(o(W)\), the depletion/support dichotomy allows only
\(o(W/H)\) distinct fixed residual values.  Its deepest-upper support is
therefore \(o(W/H)\), whereas (4.2) is \((1-o(1))W\).

This exactly separates the two sides of the dichotomy:

\[
 \boxed{
 \begin{array}{c|c|c}
 &\text{cheap fixed residual}&\text{long consuming strips}\\ \hline
 \text{deep upper masks/component}&1&2\ell\\
 \text{number of components}&o(W/H)&\asymp W/(2\ell)\\
 \text{total deep support}&o(W/H)&W-o(W)\\
 \text{portal excess}&o(W)&o(W).
 \end{array}}
 \tag{5.4}
\]

---

## 6. A proof-method ceiling at the same order

The order \(\log m/\log\log m\) is not accidental for this projected-strip
argument.

Suppose one uses the same two-row strip hypergraph, independent exact-state
initialization, and the displayed quantitative matching residual (2.2).
If a positive fraction of the middle layer is covered, the depletion ledger
forces

\[
 H/\ell\longrightarrow0
 \tag{6.1}
\]

in order that portal excess be \(o(W)\).

On the other hand the maximum codegree has the elementary lower bound

\[
 \Gamma\ge\frac{2D_0}{m^2}.
\tag{6.2}
\]

Indeed every strip through a fixed middle mask supplies its two cyclic
Johnson neighbours, and the stabilizer is transitive on the \(m^2\)
Johnson neighbours.  If the displayed quantitative matching theorem is
applicable, its codegree hypothesis gives

\[
 \frac{C\log D}{D}=o(e^{-2K})=o(1),
\]

so its permitted relative degree error

\[
 \frac{20(D^2C\log D)^{1/3}}D
 =20\left(\frac{C\log D}{D}\right)^{1/3}
\]

tends to zero.  Since the exact minimum degree is \(D_0\), the required
near-regularity therefore forces \(D_0=(1-o(1))D\).  Thus, within this
matching certificate, (6.2) becomes

\[
 \Gamma\ge(2-o(1))\frac D{m^2}.
 \tag{6.2a}
\]

Consequently the normalized residual factor in (2.2) is at least

\[
 K\exp\!\left(-(2+o(1))\frac{\log m}{K}\right),
 \qquad K=4\ell,
 \tag{6.3}
\]

up to subexponential logarithmic terms.  For this displayed certificate to
tend to zero it is necessary that

\[
 \frac{\log m}{2\ell}-\log\ell\longrightarrow+\infty.
 \tag{6.4}
\]

In particular

\[
 \ell=O\!\left(\frac{\log m}{\log\log m}\right).
 \tag{6.5}
\]

Combining (6.1) and (6.5) gives

\[
 \boxed{
 H=o\!\left(\frac{\log m}{\log\log m}\right).}
 \tag{6.6}
\]

Thus Theorem 4.1 reaches the full order permitted by this particular
quantitative projected-strip matching certificate.  This is a
**proof-method ceiling**, not a nonexistence theorem for projected-strip
matchings and certainly not an obstruction to general MTF trajectories.

---

## 7. Relation to rotor/Euler trajectories and global portals

The schedule (3.1)--(3.2) is a deterministic delayed-deletion trajectory.
It has a particularly transparent cooldown law:

\[
 \text{arrival at time }i
 \quad\Longrightarrow\quad
 \text{departure at time }i+\ell.
 \tag{7.1}
\]

This is much stronger than the required delay \(H+1\).  It makes the
rank-\((m+H)\) flag itself a sliding cyclic interval, so distinct-target
extraction is performed by the hypergraph matching before the MTF paths are
emitted.

An Euler circuit in the full rotor graph realizes the correct symmetric
average but repeats Boolean targets with large multiplicity.  The present
construction takes the complementary approach: it first extracts disjoint
middle and deepest-upper rows and only then invokes the literal MTF lift.
It therefore gives a genuine single-copy distinct-target extraction, albeit
for two controlled ranks rather than the entire Gaussian band.

The audited global-portal theorem proves that high-incidence endpoint flags
exist at the scale \(W/\sqrt m\), but leaves their stateful fusion open.
Theorem 4.1 proves that stateful fusion itself is not an obstruction at every
growing depth: nearly all middle owners can lie in super-\(H\)-long legal
components with negligible portal excess and nearly complete deepest-upper
support.  What remains absent is correlation with the product-box incidence
selection needed for a global integral support resolution, together with
simultaneous distinct-target control of all intermediate ranks.  The next
two theorems nevertheless show that one common relabeling supplies the
correct aggregate product-box incidence inside the already fused endpoints.

### Theorem 7.1 -- one relabeling makes almost every endpoint box-rainbow

Fix any partition of the \(2m\) coordinates into three blocks, fix an SCD
in each block, and let their Cartesian products be the resulting partition
of the Boolean lattice into three-chain product boxes.  There is one common
coordinate relabeling of the component family in Theorem 4.1 for which the
aggregate number of pairs of masks which

* belong to the same canonical radius-\(H\) endpoint flag, and
* lie in the same product box

is

\[
 \boxed{O(HW/m)=o(W).}
 \tag{7.2}
\]

Consequently all but \(o(W)\) of the selected middle-owner endpoints have
their entire \((2H+1)\)-mask canonical band flag in \((2H+1)\) distinct
product boxes.

#### Proof

Take two masks in one saturated endpoint flag whose ranks differ by
\(g\), where \(1\le g\le2H\).  Under a uniformly random common coordinate
permutation, their image is a uniformly random nested pair of the same
ranks.  Conditional on the lower image, its \(g\) new coordinates are
uniform among at least

\[
 \binom{m-H}{g}
\]

choices.  Inside the unique product box of the lower image, a \(g\)-step
extension is specified by its three nonnegative factor-chain advances, so
there are at most \(\binom{g+2}{2}\) such extensions.  The expected number
of same-box pairs in one flag is therefore at most

\[
 \beta_{m,H}
 :=\sum_{g=1}^{2H}(2H+1-g)
   \frac{\binom{g+2}{2}}{\binom{m-H}{g}}.
 \tag{7.3}
\]

For

\[
 a_g=\frac{\binom{g+2}{2}}{\binom{m-H}{g}},
\]

one has

\[
 \frac{a_{g+1}}{a_g}
 =\frac{g+3}{m-H-g}
 \le\frac{2H+2}{m-3H+1}=o(1),
\]

uniformly in the displayed range, while \(a_1=3/(m-H)\).  Hence

\[
 \beta_{m,H}=O(H/m).
 \tag{7.4}
\]

The component family has \(2\ell p\le W\) selected endpoints.  Linearity
of expectation gives expected aggregate collision-pair count
\(O(HW/m)\), so one common relabeling attains that bound.  A flag which is
not box-rainbow contributes at least one collision pair, proving the final
claim.  Relabeling preserves the strip matching, the exact MTF recurrence,
and global distinctness of all selected masks.  \(\square\)

This theorem concerns the complete product-box partition: it does not claim
that the resulting masks belong to any separately prescribed DRAY or other
special target family.  It supplies product-box dispersion for the literal
flags already carried by the long components.

### Theorem 7.2 -- positive-density incidence in the dominant target family

Assume for this statement that \(2m=3s\), and use the fixed three-block
dominant target family \(\mathcal T\) from the audited global-portal
construction.  One common coordinate relabeling of the component family in
Theorem 4.1 has both

\[
 \boxed{\Omega(HW)}
 \tag{7.5}
\]

distinct endpoint--target-box incidences with targets in \(\mathcal T\),
and aggregate same-box collision-pair count \(O(HW/m)\).  Consequently
\(\Omega(W)\) already-fused component endpoints each meet \(\Omega(H)\)
distinct \(\mathcal T\)-boxes.

#### Proof

The dominant boxes have factor-chain heights in the fixed windows

\[
 p,q\in[\sqrt s,1.1\sqrt s],
 \qquad r\in[3\sqrt s,3.1\sqrt s].
\]

Their plateau half-width is at least \(0.4\sqrt s\), each plateau layer
has at least \(s\) masks per box, and their number is

\[
 (\kappa_L^2\kappa_H+o(1))W_s^3
\]

for fixed positive constants \(\kappa_L,\kappa_H\).  Since
\(sW_s^3/W\) tends to a positive constant and \(H=o(\sqrt m)\), there is
an absolute \(c>0\) such that, for every \(|d|\le H\),

\[
 \left|\mathcal T\cap\binom{[2m]}{m+d}\right|\ge cW
 \tag{7.6}
\]

for all sufficiently large \(m\).

Let \(E=2\ell p=W-o(W)\) be the number of selected endpoints and let
\(X_\sigma\) count, with endpoint multiplicity, the masks in their
\((2H+1)\)-flags which a common relabeling \(\sigma\) sends into
\(\mathcal T\).  Uniform relabeling is transitive on every rank, so (7.6)
gives

\[
 \mathbb E X_\sigma\ge c(2H+1)E=\Omega(HW).
 \tag{7.7}
\]

Also \(0\le X_\sigma\le(2H+1)E\).  Hence the elementary bounded-variable
estimate gives a constant \(c_0>0\) for which

\[
 \Pr\{X_\sigma\ge c_0HW\}\ge c_0.
 \tag{7.8}
\]

Let \(Y_\sigma\) be the complete same-product-box collision-pair count of
Theorem 7.1.  Its proof gives \(\mathbb E Y_\sigma=O(HW/m)\).  Markov's
inequality, with a fixed constant chosen so that its exceptional
probability is smaller than the right side of (7.8), shows that one common
\(\sigma\) satisfies simultaneously

\[
 X_\sigma=\Omega(HW),
 \qquad
 Y_\sigma=O(HW/m).
 \tag{7.9}
\]

At one endpoint, if \(u\) selected target occurrences lie in one product
box, replacing those \(u\) occurrences by their one endpoint--box
incidence loses \(u-1\le\binom u2\).  Therefore the number of distinct
endpoint--\(\mathcal T\)-box incidences is at least
\(X_\sigma-Y_\sigma=\Omega(HW)\), proving (7.5).

Finally every endpoint has degree at most \(2H+1\).  A family of at most
\(W\) endpoints with total degree \(\Omega(HW)\) and maximum degree
\(O(H)\) must contain \(\Omega(W)\) endpoints of degree \(\Omega(H)\).
All of these endpoints are already internal to the literal MTF component
words of Theorem 4.1.  \(\square\)

---

## 8. Self-audit and exact scope

The vulnerable points are the following.

1. **Projection does not create parallel edges.**  The middle row recovers
   the strip, so projecting away the other shadow rows remains simple.
2. **The degree imbalance is harmless.**  It is \(O(H^2/m)\), far below
   the allowed cube-root error in the quantitative matching theorem.
3. **The matching controls actual masks.**  The two ranks are disjoint
   vertex parts, and selected strips are disjoint in each part.  Therefore
   (4.2) counts support, not multiplicity.
4. **The cut loses no upper masks.**  The initial queue contains the cyclic
   past departures, and terminal dummy departures provide virtual cyclic
   closure.  Equation (3.6) holds also at the two linear boundaries.
5. **Residual consumption is literal.**  The \(\ell-H\) active points of
   the initial residual all arrive.  The fixed opposite core \(D\) is the
   terminal residual and has size strictly below \(m-H\).
6. **Portal excess is not being hidden.**  Every component is initialized
   independently, so (4.3) is an explicit upper bound.  The depletion
   theorem gives the matching lower bound (5.1).
7. **No full-band claim is made.**  Intermediate canonical masks are
   physically exposed, but their collisions between different components
   are not controlled by the two-row matching.
8. **No Gaussian claim is made.**  At \(H=A\sqrt m\), long consuming
   components remain the correct surviving architecture, but the projected
   matching theorem used here gives no such factor.

---

## 9. A sharp obstruction to the explicit linear-code cycle tiling

There is a separate prescribed-scale middle factor in the project: when

\[
 \ell=2^t,
\]

the standard pair-flip cycle \(P_\ell\subset\mathbb F_2^\ell\) tiles the
orientation cube by the translations

\[
 \{P_\ell+k:k\in K\},
 \qquad
 K=\ker\phi,
 \qquad
 \operatorname{codim}K=t+1.
 \tag{9.1}
\]

This gives extremely long components at a prescribed Gaussian \(H\), but
the following theorem shows that the unchanged translation tiling cannot
supply many deepest-upper masks.

### Theorem 9.1 -- translation-kernel shadow collapse

Assume \(H<\ell\).  In the tiling (9.1), the number of distinct depth-\(H\)
upper pair-faces is at most

\[
 \boxed{
 2^\ell\min\left\{1,\frac{2\ell}{2^H}\right\}.}
 \tag{9.2}
\]

The same relative bound holds in every product extension to
\(\mathbb F_2^s\), \(s\ge\ell\).  Consequently, in any outer construction
in which these fixed-kernel product extensions contain \(W-o(W)\) middle
owners, if

\[
 H-\log_2\ell\longrightarrow\infty,
 \tag{9.3}
\]

then the explicit fixed-kernel cycle factor from the linear-code tiling has
only \(o(W)\) distinct canonical depth-\(H\) upper masks, even though it may
contain \(W-o(W)\) middle owners.

#### Proof

At one directed position \(p\) of the standard cycle, let \(J(p)\) be the
set of the preceding \(H\) flipped pair-coordinates.  Since \(H<\ell\),
these coordinates are distinct.  The associated upper mask is the
\(H\)-face

\[
 p+V_{J(p)},
 \tag{9.4}
\]

where \(V_J\) is the coordinate subspace supported on \(J\): the coordinates
in \(J\) are full pairs, and all coordinates outside \(J\) retain their
orientation.

For two translations \(k,k'\in K\), the faces at the same cycle position
coincide precisely when

\[
 k-k'\in V_{J(p)}.
 \tag{9.5}
\]

By the dimension inequality,

\[
 \dim(K\cap V_{J(p)})
 \ge \dim K+H-\ell
 =H-t-1.
 \tag{9.6}
\]

Thus, when \(H>t+1\), every face at a fixed position has at least

\[
 2^{H-t-1}=\frac{2^H}{2\ell}
 \tag{9.7}
\]

translation preimages.  There are \(2\ell|K|=2^\ell\) total state
occurrences.  Dividing by (9.7) proves (9.2); when \(H\le t+1\), use the
trivial bound \(2^\ell\).

In a product extension, the inactive coordinate word is fixed on each
fiber, so faces from different fibers are distinct and both the occurrence
count and the upper bound multiply by \(2^{s-\ell}\).  Summing the bound over
all middle-layer orientation strata can only overcount global Boolean upper
masks.  By the stated \(W-o(W)\) owner hypothesis, the selected product
extensions contribute \(o(W)\) support; any omitted or separately repaired
owners contribute at most \(o(W)\) further masks.  In the prescribed-scale
factor below, the needed owner hypothesis follows from the audited
low-split-stratum estimate.  Equation (9.3) therefore gives global support
\(o(W)\).
\(\square\)

For the explicit prescribed-scale choice

\[
 H\asymp\sqrt{m\log m},
 \qquad
 \ell\asymp m^{3/4},
\]

the collapse factor in (9.2) is exponentially small in \(H\).  Thus the
linear-code tiling solves the long-component/portal part at that scale but
fails the distinct deepest-shadow part in its unchanged fixed-kernel form.
Indeed

\[
 \frac{2\ell\,2^{-H}W}{N_H}
 =\exp\!\left(
 -H\log2+\frac{H^2}{m}+O(\log\ell)+o(1)
 \right)=o(1),
 \tag{9.8}
\]

so it realizes only \(o(N_H)\) of the available deepest-upper masks.  The
same conclusion holds at every fixed Gaussian depth \(H=A\sqrt m\) with
this \(\ell\).
A successful Gaussian construction must vary active frames or translation
kernels between cycles, or abandon translation tilings altogether.

The exact conclusion is therefore

\[
 \boxed{
 \begin{gathered}
 H=o(\log m/\log\log m),\ H\to\infty:\\
 W-o(W)\text{ middle owners and }N_H-o(W)\text{ distinct deepest-upper
 masks}\\
 \text{lie on }o(W/H)\text{ residual-consuming canonical MTF components,}\\
 \text{each of length }\omega(H),\text{ with total portal excess }o(W).
 \end{gathered}}
\]
