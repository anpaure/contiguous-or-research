# AD9: positive durable-flag fusion into one literal growing-band word

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running local job is used.

## 0. The positive theorem

Put

\[
n=2m,\qquad
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
B=\frac{W}{m+1}.
\tag{0.1}
\]

Let \(1\le H<m\).  Start with the exact odd-cut forest \(F_0\), which
has \(B\) directed complementary Johnson paths and partitions the \(W\)
middle owners.  Prescribe lifetimes

\[
\tau:\binom{[2m]}m\longrightarrow\{0,1,\ldots,H\}
\tag{0.2}
\]

in globally contiguous blocks of sizes

\[
N_0-N_1,\ N_1-N_2,\ldots,\ N_{H-1}-N_H,\ N_H
\tag{0.3}
\]

along the concatenated directed paths.

Assume there is a feasible pair of exact lower and upper-complement flag
systems \((\mathbf L,\mathbf R)\).  For an initial edge
\(e=v\to w\), put

\[
r(e)=\min\{\tau(v),\tau(w)\},
\qquad
E^\circ=\{e:r(e)\ge1\}.
\tag{0.4}
\]

The corrected durable set is

\[
\begin{aligned}
E^{\rm dur}(\mathbf L,\mathbf R)
=\{e=v\to w\in E^\circ:{}&
L_{h+1}(v)=L_h(v)\cap L_h(w),\\
&R_{h+1}(w)=R_h(v)\cap R_h(w)\\
&\text{for all }0\le h<r(e)\}.
\end{aligned}
\tag{0.5}
\]

Let

\[
D=E^\circ\setminus E^{\rm dur}(\mathbf L,\mathbf R),
\qquad K=|D|.
\tag{0.6}
\]

### Theorem 0.1 (positive cross-component literal fusion)

There is one literal contiguous-OR word which covers every mask in the
growing central band

\[
m-H,m-H+1,\ldots,m+H
\tag{0.7}
\]

and has exact basic length

\[
\boxed{
L_{\rm basic}=W+2\sum_{S}r(S),}
\tag{0.8}
\]

where the sum runs over at most

\[
\boxed{B+K+H}
\tag{0.9}
\]

constant-radius rotor segments and \(r(S)\) is the common owner lifetime
on segment \(S\).  In particular,

\[
\boxed{
L_{\rm basic}
\le W+2H(B+K+H).}
\tag{0.10}
\]

Every flag of every owner is a literal suffix interval ending at one shared
principal position for that owner.  Thus the word has one chronology, one
integral owner assignment, and no trace-repair appendix.

There is also an occurrence-faithful version.  By adding at most

\[
2(B+K+H)
\tag{0.11}
\]

single-letter witnesses, every original first-band meet and join can be
kept attached to its original forest edge.  Its length satisfies

\[
\boxed{
L_{\rm occ}
\le
W+2H(B+K+H)+2(B+K+H).}
\tag{0.12}
\]

The added witnesses are literal masks.  The theorem does not assert that
their larger overlapping interval-hull geometry is unchanged.

For fixed \(A>0\), take

\[
H=\lceil A\sqrt m\rceil.
\tag{0.13}
\]

If the flag pair can be chosen with

\[
K=o_A(W/H),
\tag{0.14}
\]

then the number of rotor segments is \(o_A(W/H)\), the number of physical
hard-reset boundaries is \(o_A(W/H)\), the number of labelled
original-edge seams carrying explicit witnesses is \(o_A(W/H)\), and

\[
\boxed{L_{\rm occ}=W+o_A(W).}
\tag{0.15}
\]

This is the requested positive fusion theorem.  Hypothesis (0.14), and
the existence of the flag pair for the prescribed lifetime blocks, remain
unproved.  Therefore the theorem is a quantitative constant-one
composition, not a proof of the constant-one conjecture.

---

## 1. Exact flag states

For

\[
X_h=\{v:\tau(v)\ge h\},
\]

the lower maps are bijections

\[
L_h:X_h\longrightarrow\binom{[2m]}{m-h},
\tag{1.1}
\]

and the upper-complement maps are bijections

\[
R_h:X_h\longrightarrow\binom{[2m]}{m-h}.
\tag{1.2}
\]

They obey

\[
L_{h+1}(v)\subset L_h(v),
\qquad
R_{h+1}(v)\subset R_h(v).
\tag{1.3}
\]

For an owner \(v\) of lifetime \(r=\tau(v)\), let

\[
\ell_h(v)=L_h(v)\setminus L_{h+1}(v),
\qquad
u_h(v)=R_h(v)\setminus R_{h+1}(v)
\tag{1.4}
\]

for \(0\le h<r\).  These are single coordinates.  The full radius-
\(r\) state is

\[
\omega_r(v)=
\bigl(
L_r(v);
\ell_{r-1}(v),\ldots,\ell_0(v),
u_0(v),\ldots,u_{r-1}(v);
R_r(v)
\bigr).
\tag{1.5}
\]

Its saturated chain consists exactly of

\[
L_r(v),\ldots,L_1(v),v,
[2m]\setminus R_1(v),\ldots,[2m]\setminus R_r(v).
\tag{1.6}
\]

Because (1.1)--(1.2) are bijections, the chains (1.6), over all owners,
cover each rank in (0.7) exactly once.

The restriction \(E^{\rm dur}\subseteq E^\circ\) in (0.5) is essential:
without it, lifetime-zero edges satisfy the displayed identities vacuously
and corrupt the deletion count.

---

## 2. Cutting to constant-radius durable segments

Define the set of genuine lifetime-change edges

\[
J=\{v\to w\in E(F_0):\tau(v)\ne\tau(w)\}.
\tag{2.1}
\]

### Lemma 2.1 (at most \(H\) lifetime seams)

\[
\boxed{|J|\le H.}
\tag{2.2}
\]

#### Proof

The \(H+1\) lifetime classes are consecutive intervals in the global
concatenation.  There are \(H\) interfaces between consecutive classes.
An interface either lies between two original path lists, in which case it
crosses no edge of \(F_0\), or lies inside one path list, in which case it
crosses exactly one edge.  Thus at most one genuine edge belongs to each
interface. \(\square\)

Cut every edge in

\[
D\cup J.
\tag{2.3}
\]

Since \(F_0\) has \(B\) path components, the resulting forest has exactly

\[
B+|D\cup J|
\tag{2.4}
\]

segments and therefore at most \(B+K+H\).  Every segment has a constant
lifetime \(r(S)\).

### Lemma 2.2 (every surviving segment is a genuine rotor path)

Let \(v\to w\) be an edge remaining inside a segment of common radius
\(r\).  Then

\[
\omega_r(v)\longrightarrow\omega_r(w)
\tag{2.5}
\]

is a genuine directed radius-\(r\) rotor edge.

#### Proof

If \(r=0\), (2.5) is the original directed Johnson edge, which is exactly
the radius-zero rotor rule.

Suppose \(r\ge1\).  Then the common lifetime of the edge is \(r\), so it
belongs to \(E^\circ\).  It was not cut in \(D\), hence it is durable.
For every \(0\le h<r\), it satisfies

\[
L_{h+1}(v)=L_h(v)\cap L_h(w),
\qquad
R_{h+1}(w)=R_h(v)\cap R_h(w).
\tag{2.6}
\]

At \(h=0\), these are exactly the two forced endpoint choices that lift
the Johnson edge to radius one.  Assume inductively that the radius-
\(h\) states are rotor neighbours.  The exact one-edge lift criterion says
that (2.6) at level \(h\) is necessary and sufficient for their radius-
\((h+1)\) extensions to remain rotor neighbours; endpoint injectivity
supplies the two remaining non-equalities.  Induction through \(h=r-1\)
proves (2.5). \(\square\)

Thus the construction has performed the cross-component synchronization:
after only \(K+H\) possible new cuts, every surviving piece is one
physical constant-radius MTF trajectory.

---

## 3. One exact literal chronology

We reprove the hard-reset word because this is the decisive literal step.

### Lemma 3.1 (exact word for one rotor segment)

Let

\[
\omega_r(v_1)\to\omega_r(v_2)\to\cdots\to\omega_r(v_t)
\tag{3.1}
\]

be a directed radius-\(r\) rotor path.  It has a literal word of exact
length

\[
\boxed{t+2r}
\tag{3.2}
\]

in which every member of every chain \(\omega_r(v_i)\) is a suffix OR
ending at one principal position for \(v_i\).

#### Proof

Write the first state as

\[
\omega_r(v_1)=(L;z_1,\ldots,z_{2r};R).
\]

Begin the word with

\[
\{z_{2r}\},\{z_{2r-1}\},\ldots,\{z_1\},L.
\tag{3.3}
\]

The suffix ORs ending at the last entry of (3.3) are precisely the
\(2r+1\) members of the first saturated chain.

If the rotor update removes \(x\in L\) and inserts \(y\in R\), append the
new lower core

\[
L'=L-\{x\}+\{y\}.
\]

For \(r=0\), this new core alone is the entire successor state.  Assume
now that \(r\ge1\).

The augmented last-occurrence state at this new endpoint is exactly the
successor state: its useful prefix is

\[
L',\{x\},\{z_1\},\ldots,\{z_{2r-1}\},
\]

and its residual union is \(R-\{y\}+\{z_{2r}\}\).  Equivalently, the
full augmented last-occurrence partition still has \(\{z_{2r}\}\) as
the next refined tail block, but the radius-\(r\) state coarsens that block
into the residual.  Therefore the suffix ORs ending at \(L'\) expose the
entire successor chain.  Repeat one appended core for each later owner.

The initialization uses \(2r+1\) entries and the remaining \(t-1\)
owners use one each, for total \(t+2r\). \(\square\)

### Proof of Theorem 0.1, basic form

Apply Lemma 3.1 to every segment supplied by Lemma 2.2 and concatenate the
segment words.  Intended suffix intervals lie wholly within their own
segment words, so concatenation cannot destroy them.  If segment \(S\)
has \(t(S)\) owners, the total length is

\[
\sum_S(t(S)+2r(S))
=W+2\sum_Sr(S),
\]

which proves (0.8).  Equations (0.9)--(0.10) follow from
\(r(S)\le H\).

By (1.6), every band mask occurs among the exposed chain suffixes.  No
separately optimized rank, fractional owner, or appended trace word is
used.  This proves the basic theorem. \(\square\)

---

## 4. Optional occurrence-faithful first-band seams

The basic word already covers the complete first band exactly because the
flag chains form a band SCD.  We now preserve, in addition, the original
edge-by-edge first-band certificate.

The lifetime-zero class has exact size

\[
|\tau^{-1}(0)|=N_0-N_1=B.
\tag{4.1}
\]

Let

\[
E_0=E(F_0[\tau^{-1}(0)]).
\tag{4.2}
\]

Since \(F_0[\tau^{-1}(0)]\) is a forest on \(B\) vertices,

\[
\boxed{|E_0|\le B.}
\tag{4.3}
\]

Cut the edges in \(E_0\) as well.  These are radius-zero segments, so the
new cuts add no hard-reset toll: in (0.8), their radius is zero before and
after splitting.

Put

\[
Q=D\cup J\cup E_0.
\tag{4.4}
\]

Then

\[
|Q|\le B+K+H.
\tag{4.5}
\]

Order the resulting segments in their original path order.  For every cut
edge

\[
e:v\to w,
\]

insert the two literal masks

\[
v\cap w,
\qquad
v\cup w
\tag{4.6}
\]

at its macro-seam.  Intended suffix intervals in the two neighbouring
segment words remain internal to those words, so the insertion changes no
previous certificate.

If an original edge is not in \(Q\), its endpoints have the same lifetime
\(r\ge1\), and the edge is durable.  The level-zero identities give

\[
L_1(v)=v\cap w,
\qquad
[2m]\setminus R_1(w)=v\cup w.
\tag{4.7}
\]

Thus its old meet and join already occur at the source and target principal
endpoints of the same rotor segment.  Edges in \(Q\) have the explicit
single-letter witnesses (4.6).  Hence every original edge colour is
preserved with its edge identity.

There are two added positions per edge of \(Q\).  Equations
(0.8), (4.3), and (4.5) prove (0.11)--(0.12).

This is occurrence-faithful literalization.  A single-letter witness is a
valid interval, but it does not retain the old multi-interval hull pattern
of the frozen facet braid or the old shared principal endpoint at that cut
edge.

---

## 5. Exact seam and asymptotic ledger

Choose a flag pair maximizing the corrected durable set.  The audited
first-failure identity gives

\[
K=K_H^{\min}
=|E^\circ|-
\max_{\mathbf L,\mathbf R}|E^{\rm dur}(\mathbf L,\mathbf R)|.
\tag{5.1}
\]

The number of constant-radius rotor segments in the basic word is at most

\[
P_{\rm basic}=B+K+H.
\tag{5.2}
\]

The occurrence-faithful splitting adds at most \(B\) radius-zero pieces,
so

\[
P_{\rm occ}\le2B+K+H.
\tag{5.3}
\]

Here \(P_{\rm occ}\) counts rotor pieces, hence hard-reset starts.  Their
linear concatenation has \(P_{\rm occ}-1\) inter-piece boundaries.  The
smaller set of labelled original-edge macro-seams carrying the insertions
(4.6) has size

\[
|Q|\le B+K+H.
\tag{5.3a}
\]

Now fix \(A>0\) and let \(H=\lceil A\sqrt m\rceil\).  Assume

\[
K=o_A(W/H).
\tag{5.4}
\]

Then

\[
B=\frac{W}{m+1}=o(W/H),
\qquad
H=o(W/H),
\tag{5.5}
\]

because \(W\) is exponential in \(m\).  Hence

\[
\boxed{P_{\rm occ}=o_A(W/H),}
\tag{5.6}
\]

which is stronger than merely \(o(W)\) seams.

The exact excess in (0.12) is bounded by

\[
\begin{aligned}
L_{\rm occ}-W
&\le2HB+2HK+2H^2+2B+2K+2H\\
&=o_A(W).
\end{aligned}
\tag{5.7}
\]

Indeed,

\[
2HB=O_A(W/\sqrt m),
\qquad
2HK=o_A(W),
\qquad
2H^2=O_A(m),
\tag{5.8}
\]

and the remaining terms are smaller.  This proves (0.15).

The quantifiers are: for each fixed \(A>0\), the same construction must
exist for every sufficiently large \(m\), with the ratio
\(HK/W\to0\).  Only after taking the fixed-\(A\) limsup may one send
\(A\to\infty\).

Using the already audited outer-tail word, the conditional band theorem
gives

\[
\limsup_{m\to\infty}
\frac{\nu(2m)}{W}
\le1+O((1+A^2)e^{-A^2}).
\tag{5.9}
\]

Letting \(A\to\infty\), and then using the standard even-to-odd transfer,
would prove the sharp constant-one theorem.  This implication remains
conditional on feasible flags satisfying (5.4).

---

## 6. Minimal tube/cone input and proved boundary

The construction uses only the following audited dynamic facts.

1. The durable universe is \(E^\circ\), not all initial edges.
2. For fixed flags, every nondurable edge has one first failed level and is
   charged exactly once.  Hence \(|D|=K\).
3. The two endpoint intersection identities are necessary and sufficient
   for one inherited edge to lift by one more radius; iterating them proves
   Lemma 2.2.

The triangular tube inequality

\[
\Delta_q^\pm\le\sum_{s<q}(q-s)k_s
\]

and the cone transversal are consistent with this construction but are not
needed to literalize the surviving constant-radius segments.  No
rank-goodness inference from mere departure distinctness is used.

### Proved

- Exact constant-radius segmentation with at most \(B+K+H\) pieces.
- Exact hard-reset length \(W+2\sum_Sr(S)\).
- One literal chronology exposing every band flag at a shared owner
  endpoint.
- Optional edge-identity preservation for the full first band at only
  \(2(B+K+H)\) extra positions.
- The \(W+o_A(W)\) conclusion under the explicit deletion hypothesis
  \(K=o_A(W/H)\).

### Unproved

- Feasibility of both exact flag systems for the prescribed globally
  contiguous lifetime assignment.
- The sharp durable agreement estimate \(K_H^{\min}=o_A(W/H)\).

Thus the positive fusion and literal chronology are complete.  The sole
remaining constant-one gate in this route is the existence of an almost
fully durable exact flag pair; no trace-condensation or further
cross-component synchronization lemma remains after that pair is supplied.
