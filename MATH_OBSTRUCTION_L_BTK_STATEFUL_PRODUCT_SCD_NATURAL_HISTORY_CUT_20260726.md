# A natural five-edge history cut in the BTK product-SCD endpoint digraph

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver,
or web input is used.

## 0. Exact result

Let (A\mathbin{\dot\cup}B) have (|A|=|B|=m), put

\[
                         W=\binom{2m}{m},
\]

and use the standard BTK/Greene--Kleitman symmetric-chain
decomposition on both halves.  Its rank-(m) product diagonals form a
partition ({\cal P}) of the middle layer into

\[
 c_m^2,\qquad c_m=\binom m{\lfloor m/2\rfloor},
\tag{0.1}
\]

monotone Johnson paths.  Write (h(P)) for the number of edges of
(P).

Consider the exact two-queue (H)-memory endpoint digraph: a proposed
seam and the complete outgoing product path are read edge by edge, and
an insertion followed by a removal of the same coordinate at inclusive
span at most (H) is forbidden.  This is already the exact one-sided
lower-shadow condition; no upper-shadow condition is needed below.

The main theorem is

\[
 \boxed{
  7\le h(P)\le H-8
  \quad\Longrightarrow\quad
  P\text{ has neither a predecessor nor a successor product atom}.}
\tag{0.2}
\]

Here an atom is retained whole, may be oriented in either direction,
and atoms are joined only by literal Johnson seams between their
endpoints.  The history which kills the seam is not adversarially
invented: it is the terminal five-edge suffix of the preceding atom
itself.

Consequently, if

\[
                  H/\sqrt m\longrightarrow\infty,
                  \qquad H\le m,
\tag{0.3}
\]

then every whole-atom route cover has at least

\[
 \boxed{
 (1-o(1))c_m^2
   =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}}
\tag{0.4}
\]

components.  In the lifted endpoint graph there is an explicit family
of

\[
 \left({4\over\sqrt\pi}+o(1)\right){W\over\sqrt m}
\tag{0.5}
\]

naturally reachable oriented endpoint states with empty out-neighborhood.
Thus ordinary Posa rotations or alternating cycles on the whole-atom
endpoint graph cannot give (O(W/m)) components.  The component collar
would instead be of order

\[
 Hc_m^2=\Theta\!\left({H\over\sqrt m}W\right).
\tag{0.6}
\]

This is a concrete obstruction for the fixed BTK product-SCD atlas.  It
does not rule out a moving SCD, a second physical frame, or a compound
exchange which cuts and reroutes atoms internally.  In particular, raw
set complementation does not preserve one SCD.  Enlarging the catalogue
by a raw-complemented atlas introduces cross-atlas seams which are not
covered by (0.2).

The exact escape forced by the proof is also clear.  At a fused endpoint
one must destroy the original five-edge terminal fringe, expose an
internal port after splitting the atom, insert a genuinely flushing
bridge, or change the active-chain frame.  Merely permuting whole atoms
or reversing a terminal segment of the atom-order path does not change
the obstruction.

## 1. The one-sided memory test and the off-by-one convention

Write a Johnson word as

\[
                         X_t=X_{t-1}-a_t+b_t.
\tag{1.1}
\]

Before edge (t), the insertion queue contains the labels (b_s) from
the preceding (H-1) edges, with ages retained.  The edge is lower
legal exactly when

\[
                         a_t\notin\{b_s:t-H+1\le s<t\}.
\tag{1.2}
\]

Indeed, if (b_u=a_v), the inclusive residence span is

\[
                         \rho=v-u+1.
\tag{1.3}
\]

The intersection of the owners in that (ho)-edge window has size at
least (m-\rho+1), rather than (m-\rho).  Conversely, every lower-rank
failure contains such an insertion--removal pair.  Therefore (1.2) is
necessary and sufficient for the exact one-sided shadow ranks through
depth (H).

The equality case matters: an edge (u) remains relevant to edge (v)
when (v-u+1=H).  Thus a bound (ho\le H), not (ho<H), rejects
the extension.

## 2. BTK active tails change in at most four positions

For a binary word (w=w_1\cdots w_m), put

\[
 D_w(t)=\sum_{i\le t}(2w_i-1),\qquad D_w(0)=0.
\tag{2.1}
\]

The unpaired ones in the BTK parenthesis matching are exactly the strict
ascending record times of (D_w).  If (|w|=k\ge m/2) and

\[
                         h=2k-m,
\tag{2.2}
\]

then the (h) coordinates inserted between the symmetric rank-((m-k))
and rank-(k) members of the BTK chain are the last (h) strict record
times.  Denote this set by (I_h(w)).

We use the following exact stability fact.

### Lemma 2.1 (record-tail stability)

Let (w') be the (A)-restriction of a Johnson neighbor of a middle
owner whose (A)-restriction is (w).  Put

\[
 h=2|w|-m,qquad h'=2|w'|-m,
\]

and assume (h,h'>0).  Then

\[
                  |I_h(w)\setminus I_{h'}(w')|\le4.
\tag{2.3}
\]

#### Proof

If the Johnson edge is internal to (B), nothing changes.  If it is
internal to (A), the two height walks differ by (2) on one interval
and agree outside it.  Relative to the old prefix maximum, this can add
or remove at most two record levels at the first end of the interval and
at most two after the walks reunite.  Hence their complete record-time
sets have symmetric difference at most four.

For a cross-half edge, one bit of (w) changes.  The height walk is
translated by (2) on a suffix, so at most two record levels change;
also (h'=h\pm2).  Passing from the full record sets to their terminal
tails can discard at most the two elements caused by this length change.
Thus the one-sided loss from the old (h)-tail is at most four in every
case.  This is (2.3).  \(\square\)

In particular, every five-subset (F\subseteq I_h(w)) satisfies

\[
                         F\cap I_{h'}(w')\ne\varnothing.
\tag{2.4}
\]

The five in (2.4) is the source of the constant-width history cut.

## 3. Exact high-end obstruction

A product diagonal of length (h) has (A)-ranks

\[
              {m-h\over2},{m-h\over2}+1,\ldots,{m+h\over2}.
\tag{3.1}
\]

When it is traversed from low to high, it inserts exactly the coordinates
in its (A)-active tail (I_A(P)), one per edge, and removes distinct
(B)-coordinates.  All these insertions remain present at the high
endpoint.

Let (P) have length (h\ge5), traverse it low to high, and let (F_P)
be the five (A)-coordinates inserted on its last five edges.  Consider
any literal seam from its high endpoint (X) to a product-path endpoint
(Y).

First, (Y) must also be a high endpoint.  A high endpoint of a
positive-length path has (A)-rank ((m+h)/2), while a low endpoint of
a path of length (h') has (A)-rank ((m-h')/2).  A Johnson edge can
change (A)-rank by at most one.  For (h\ge5), these two types cannot
be adjacent.  Moreover the length (h') of the path (Q) at (Y)
satisfies

\[
                         h'\in\{h-2,h,h+2\}.
\tag{3.2}
\]

The only orientation of (Q) starting at its high endpoint is high to
low.  Lemma 2.1 and (2.4) give a coordinate

\[
                         z\in F_P\cap I_A(Q).
\tag{3.3}
\]

Both high endpoints contain (z), so the seam does not change (z).
It was inserted on one of the last five edges of (P), and the reverse
traversal of (Q) removes it on one of its (h') internal edges.  With
the seam indexed as edge (0), the insertion is at an index in
({-5,-4,-3,-2,-1}), while the removal is at an index in
({1,\ldots,h'}).  Hence its inclusive residence span is at most

\[
                         \rho\le h'+6.
\tag{3.4}
\]

We have proved:

### Theorem 3.1 (five-edge high-port lock)

The concatenation

\[
       P_{\rm low\to high}\;\Vert\;\text{seam}\;\Vert\;
       Q_{\rm high\to low}
\]

is not lower (H)-safe whenever

\[
                         h(P)\ge5,qquad H\ge h(Q)+6.
\tag{3.5}
\]

This rejection is witnessed by the naturally generated last-five-edge
queue of (P).

## 4. Exact low-end obstruction

Traverse (P) from high to low.  It now inserts its (B)-active
coordinates, and its last five edges insert a five-subset (F_P^B) of
that active tail.  A Johnson neighbor of the low endpoint is another low
endpoint when (h(P)\ge5).  Interchanging the roles of (A) and (B)
in Lemma 2.1 shows that the outgoing low-to-high path (Q) removes a
coordinate of (F_P^B).  The same index calculation gives

\[
                         \rho\le h(Q)+6.
\tag{4.1}
\]

### Theorem 4.1 (five-edge low-port lock)

The concatenation

\[
       P_{\rm high\to low}\;\Vert\;\text{seam}\;\Vert\;
       Q_{\rm low\to high}
\]

is not lower (H)-safe whenever (h(P)\ge5) and
(H\ge h(Q)+6).

Thus both possible orientations are obstructed in the same one-sided
memory queue.  Complement symmetry is not being used to manufacture the
second orientation.

## 5. Isolation and the large Hall cut

Let (P) satisfy

\[
                         7\le h(P)\le H-8.
\tag{5.1}
\]

Every product atom (Q) endpoint-adjacent to (P) has length
(h(Q)\in\{h(P)-2,h(P),h(P)+2\}).  Hence (h(Q)\ge5), and

\[
                         h(Q)+6\le H.
\tag{5.2}
\]

Theorems 3.1 and 4.1 show that (P) cannot be followed by (Q), in
either orientation.  If (Q) is proposed before (P), then
(h(Q)\ge5) and the same theorem, now applied with (Q) first, rejects
that order as well.  This proves (0.2).

For each nontrivial (P) satisfying (5.1), orient it in both directions
and retain the exact terminal two-queue state generated by its own word.
The two terminal owners are distinct.  Product diagonals partition the
middle layer, so states coming from distinct paths have distinct terminal
owners.  Let ({\cal S}_H) be this family of oriented terminal states.
Then

\[
                         N^+({\cal S}_H)=\varnothing,
\qquad |{\cal S}_H|=2|{\cal P}_H|,
\tag{5.3}
\]

where ({\cal P}_H) denotes the paths in (5.1).  Equation (5.3) is an
actual history-conditioned Hall cut.  It is stronger than a low static
endpoint degree: every state in the cut is reached by traversing its own
atomic word.

It follows immediately that no sequence of endpoint-graph Posa
rotations can use a member of ({\cal P}_H) in a component containing a
second whole atom.  Every new join produced by such a rotation is still
one of the locally forbidden joins above.  Likewise, there is no
alternating cycle supported on these endpoint incidences.

## 6. Exact census

For an admissible length (h=m-2r), the number of product paths of
exact length (h) is

\[
 P_h=\binom mr^2-\binom m{r-1}^2.
\tag{6.1}
\]

Equivalently, the number having length at least (L) is

\[
 P_{\ge L}
   =\binom m{\lfloor(m-L)/2\rfloor}^{\!2}.
\tag{6.2}
\]

The number with (h<7) is

\[
 c_m^2-P_{\ge7}=O(c_m^2/m).
\tag{6.3}
\]

The elementary central-binomial ratio bound gives

\[
 {P_{\ge L}\over c_m^2}
 \le \exp\left(-{L^2-O(L)\over m}\right).
\tag{6.4}
\]

At (L=H-8), assumption (0.3) makes the right side (o(1)).
Therefore

\[
                         |{\cal P}_H|=(1-o(1))c_m^2.
\tag{6.5}
\]

Finally,

\[
 c_m^2
 =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m},
\tag{6.6}
\]

which proves (0.4)--(0.5).  The raw endpoint census agrees: apart from
the (O(c_m^2/m)) singleton paths, every path contributes two distinct
endpoints, so the total endpoint count is

\[
 \left({4\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.
\tag{6.7}
\]

Almost all of these endpoints occur in the empty-neighborhood lifted
cut (5.3).

## 7. Relation to the linear repeat functional

The obstruction is already one-sided.  For every rejected seam there is
an insertion--removal residence of span

\[
                         \rho\le h(Q)+6=o(H)
\tag{7.1}
\]

on the super-Gaussian core.  The depth-(ho) crossing intersection has
the wrong rank.  If full exterior collars are present, the same fixed
residence invalidates at least one crossing lower occurrence at every
depth

\[
                         q=\rho,\rho+1,\ldots,H.
\tag{7.2}
\]

Thus a frozen occurrence assignment would pay at least

\[
                         H-\rho+1=H-o(H)
\tag{7.3}
\]

per attempted whole-atom fusion.  Across (Theta(W/\sqrt m)) fusions,
this is (Theta((H/\sqrt m)W)).

Equation (7.3) is an invalid-occurrence statement.  It is not, by
itself, a lower bound of that size on the number of distinct global
missing targets: different invalid occurrences may be reassigned to
other physical columns.  The rigorous conclusion for the exact
one-sided criterion is that the unmodified seam is absent from the
stateful endpoint digraph.  Converting the occurrence toll into the
linear repeat-excess objective still requires the global one-hot or Hall
cut appropriate to that objective.

## 8. Complement and escape boundary

The standard BTK decomposition is permuted by reverse-complement, not by
raw set complementation.  The obstruction above needs no symmetry: it
already rules out a small-component whole-atom route in the fixed atlas
before complement equivariance is imposed.  Reverse-complement and the
half swap carry the high-port cut to the low-port cut.

One must not infer that the union of the BTK atlas and its raw-complement
atlas has the same empty-neighborhood cut.  A seam from a BTK terminal
state to an atom of the second atlas compares two different active-tail
systems, and Lemma 2.1 does not control that cross-atlas overlap.

The proof isolates the exact escape operations.

1. **Internal exposure.**  Split an atom near an endpoint so that fewer
   than five of its original active insertions occur in the current
   (H)-memory trajectory before the new seam.  The earlier part cannot
   remain immediately before that exposed fringe, since all of its
   insertions are still younger than (H).
2. **Chronological flushing.**  Insert a long safe bridge which expires
   the obstructing active directions before the next atom.  A mere reset
   label which leaves the physical successor unchanged does not do this.
3. **Frame change.**  Use an SCD or owner recoupling whose outgoing active
   tail is not four-edit-close to the preceding BTK tail.
4. **Compound exchange.**  Alter the internal atom words and all affected
   target columns together, rather than applying an endpoint permutation
   to intact atoms.

Any positive theorem must charge and verify one of these operations.
Ordinary whole-atom Posa rotations, path reversals, and alternating-cycle
switches preserve the five-edge fringe and therefore cannot cross the
cut.

## 9. Audited boundary

Proved:

* the exact inclusive-span bound (h(Q)+6);
* a naturally reachable five-edge queue which kills every same-atlas
  continuation;
* isolation of every whole BTK product atom with
  (7\le h\le H-8);
* an empty-neighborhood lifted Hall cut on almost all raw endpoints;
* the sharp asymptotic component lower bound
  ((2/\sqrt\pi+o(1))W/\sqrt m); and
* failure of whole-atom Posa and alternating-cycle routing on this
  catalogue.

Not proved:

* a cut against cross-frame or raw-complement-atlas continuations;
* a lower bound on distinct global holes equal to the invalid-occurrence
  count;
* impossibility of internal atom splitting and recoupling;
* a barrier for an arbitrary moving SCD; or
* coefficient one.

The decisive distinction is reachability.  Earlier arbitrary-history
cuts showed that a malicious queue can isolate a narrow port.  Here the
isolating queue is forced by the atom just traversed, and it occurs on
all but (o(c_m^2)) paths of the concrete BTK product-SCD cover.
