# Iterative re-centered residence-motif descent

## An integer Lyapunov theorem, the exact `147 -> 97` ledger, and the seam-lock obstruction

Date: 2026-07-29  
Lane: K  
Status: **unconditional ordinary and wrapper-weighted monotonicity; audited strict first descent; internal radius-98 joint q1 completion is now closed, while the exterior-provider tier remains open**

## 0. Main result

For a quotient 2-factor `F`, let `H(F)` be its exact hypergraph of selected
edge-orbit sets forcing positive coordinate runs of length less than four,
and write

\[
 \tau(F)=\tau(\mathcal H(F)).
\]

Suppose `F'` is obtained from `F` by deleting

\[
 D=F\setminus F'
\]

and adding

\[
 J=F'\setminus F,
\]

with `|D|=|J|`.  If `D` hits every motif of `F`, then `J` hits every motif
of `F'`.  Consequently, if `D` is a minimum old-motif transversal,

\[
 \boxed{\tau(F')\le |J|=|D|=\tau(F).}
\tag{0.1}
\]

Thus `tau` is an integer Lyapunov function for exact minimum-transversal
rethreading.  The proof is purely local and does not depend on q1, top
residence, connectivity, or the particular factor construction.  Those
conditions remain wrapper constraints on which outgoing rethreads are
allowed.

There is also a sharp transition-level decomposition.  Put

\[
 A=J\cap\bigcup\mathcal H(F'),
\tag{0.2}
\]

and form the added-seam trace hypergraph

\[
 \mathcal S_J(F')={M\cap J:M\in\mathcal H(F')\}.
\tag{0.3}
\]

Every trace is nonempty.  If

\[
 \sigma(F,F')=\tau(\mathcal S_J(F')),
\]

then

\[
 \tau(F')\le\sigma(F,F')\le |A|\le|J|.
\tag{0.4}
\]

For an exact minimum rethread, the total drop has the identity

\[
\boxed{
\tau(F)-\tau(F')
=(|J|-|A|)+(|A|-\sigma)+(\sigma-\tau(F')).
}
\tag{0.5}
\]

The three nonnegative terms are respectively:

1. added seams lying in no new bad collar;
2. coalescence among added-seam traces; and
3. additional capture by retained edges.

For the first certified `k=16` rethread, (0.5) is exactly

\[
 \boxed{147-97=40+6+4.}
\tag{0.6}
\]

This validates iterative re-centering as a rigorous alternative to keeping
all later CEGAR rounds inside the original radius-147 sphere.  It does not
yet prove the next q1/top-valid rethread.

There is one necessary refinement.  The ordinary minimum at the new state
is 97, but every 97-edge transversal deletes edge 22511, the unique current
provider of upper-q1 colour `(1,1907)`; the exact radius-97 exposure atlas
contains no replacement.  A two-motif overlap component therefore has
ordinary local transversal number one and palette-safe local number two.
Componentwise summation gives

\[
 \boxed{\widehat\tau_{\rm pal}(F_1)=98>\tau(F_1)=97.}
\tag{0.7}
\]

The hat records that this is the exact deletion-level palette-lock potential,
not an existence proof for a completed radius-98 factor.  The subsequent
exact internal solve proves that no endpoint-balanced choice at radius 98
preserves both q1 palettes, even with top residence relaxed.  This is the
joint coloured-b-factor surcharge proved in
`MATH_THEOREM_K_K16_JOINT_PALETTE_ENDPOINT_SURCHARGE_AND_HARD_DESCENT_20260729.md`.
A global exterior-provider tier is not part of that internal no-go.  A
general completion-weighted potential is defined in Section 6.1; unlike a
static edge weighting, it is automatically monotone by reverse completion.

## 1. Exact motif locality

The physical lift of a selected quotient factor is a disjoint union of
cycles.  A positive run of length `ell<4` has a forcing collar consisting
of its entering edge, its internal edges, and its exiting edge.  After
passing to cyclic edge orbits, this is the motif used by

```
residence_motif_edge_sets(...).
```

The only structural property needed below is the following.

### Lemma 1.1 (common-collar inheritance)

Let `F,F'` be two degree-two factors on the same physical vertex set.  If a
short-run forcing collar of `F'` uses only common edges `F intersection F'`,
then the same collar, possibly read in reverse, is a short-run forcing
collar of `F`.

#### Proof

The common-edge graph is a disjoint union of paths and cycles.  Consecutive
common edges in `F'` meet at a vertex where both factors already contain
those two incident edges; degree two leaves no alternative continuation in
`F`.  Hence the whole common collar occurs consecutively in `F`, possibly
with reversed orientation.  Reversal preserves the coordinate word
`0 1^ell 0`, so it preserves the short-run witness.  QED.

The entering and exiting edges are essential here.  A statement only about
the internal `1` states would not determine the old chronology at the two
ends.

## 2. The seam-transversal theorem

### Theorem 2.1 (re-centered monotonicity)

Let `F,F'` be equal-size degree-two factors and put

\[
 D=F\setminus F',\qquad J=F'\setminus F.
\]

If `D` intersects every member of `H(F)`, then `J` intersects every member
of `H(F')`.

#### Proof

Assume that a new motif `M in H(F')` avoids `J`.  Every edge of `M` then
belongs to `F intersection F'`.  Lemma 1.1 makes `M` an old motif of `F`.
But `D` hits every old motif, while `M subseteq F'` is disjoint from `D`.
This contradiction proves `M intersection J` is nonempty.  QED.

### Corollary 2.2 (integer Lyapunov function)

If `D` is a minimum transversal of `H(F)`, then (0.1) holds.

#### Proof

Theorem 2.1 makes `J` a transversal of `H(F')`; hence

\[
 \tau(F')\le|J|=|D|=\tau(F).
\]

QED.

The exact-minimum hypothesis matters.  A rethread at radius larger than
`tau(F)` only proves `tau(F')` is at most that larger radius and need not be
monotone relative to `tau(F)`.

The q1 and top-residence conditions also matter algorithmically, but not in
the proof: if both factors satisfy a wrapper condition, the same inequality
holds inside that restricted state graph.

## 3. The seam-trace potential

Because every new motif meets `J`, its trace in (0.3) is nonempty.  A set of
added edges hits every trace if and only if it hits every new motif through
an added edge.  Therefore

\[
 \tau(F')\le\tau(\mathcal S_J(F')).
\]

The active set `A` in (0.2) hits every trace, giving (0.4) and then the
telescoping identity (0.5).

### Lemma 3.1 (singleton seam locks)

Let `r=|J|`.  Then

\[
 \sigma(F,F')=r
\]

if and only if, for every added edge `j in J`, there is a new motif `M_j`
with

\[
 M_j\cap J=\{j\}.
\tag{3.1}
\]

#### Proof

If (3.1) holds, every transversal of the trace hypergraph must contain every
`j`, so its size is at least `r`; the full set `J` gives equality.

Conversely, if no trace equals `{j}`, then every trace contains either a
different added edge or at least two added edges.  Thus `J\setminus{j}` still
hits every trace, and `sigma<=r-1`.  QED.

Hence absence of even one singleton seam lock forces strict descent:

\[
 \sigma<|J|\quad\Longrightarrow\quad\tau(F')<\tau(F).
\tag{3.2}
\]

Singleton locks are necessary for a plateau, but not sufficient.  A retained
edge can hit several private motifs simultaneously, making the last term of
(0.5) positive.

## 4. Exact plateau characterization under packing equality

Assume the new motif family satisfies

\[
 \tau(F')=\nu(F').
\tag{4.1}
\]

This holds for both certified `k=16` families in this note.

### Theorem 4.1 (seam-saturated private packing)

Under (4.1), an exact minimum rethread has

\[
 \tau(F')=\tau(F)=r
\]

if and only if `H(F')` contains `r` pairwise edge-disjoint motifs.  Such a
packing necessarily consists of one `J`-private motif per added seam:

\[
 M_j\cap J=\{j\},\qquad j\in J.
\tag{4.2}
\]

#### Proof

Theorem 2.1 gives the transversal `J`, so `nu(F')<=tau(F')<=r`.  Under
(4.1), equality `tau(F')=r` is therefore equivalent to a packing of `r`
motifs.

Every packed motif meets `J`.  Pairwise disjointness makes their intersections
with `J` disjoint.  There are `r` motifs and only `r` added edges, so each
motif uses exactly one added edge and every added edge is used.  This is
(4.2).  Conversely, an `r`-packing gives `nu(F')>=r`, while `J` gives
`tau(F')<=r`; hence equality.  QED.

Thus, on packing-perfect motif families, strict descent occurs exactly when
the seam-saturated private packing of Theorem 4.1 is absent.

Without (4.1), a private packing of size `r` still certifies a plateau, but
its absence need not: a nonpacking-perfect hypergraph can have transversal
number `r` and smaller packing number.

## 5. What cannot follow from locality alone

There is no universal constant `c<1` for which every exact minimum rethread
satisfies

\[
 \tau(F')\le c\tau(F).
\]

Indeed, the collar-locality axioms alone allow `r` disjoint old motifs, one
deleted edge in each, followed by `r` disjoint new motifs, one private added
edge in each.  Theorem 4.1's plateau certificate is then present and
`tau(F')=tau(F)=r`.  At the opposite extreme, the rethread can create no new
motif and give `tau(F')=0`.

This is an architecture-level sharpness statement: it does not assert that
every abstract plateau is realizable inside the full Johnson/q1/top wrapper.
Ruling out such a plateau there is precisely the additional theorem needed
for unconditional termination.

## 6. Iterated re-centering

Let

\[
 F_0,F_1,F_2,\ldots
\]

be a sequence of wrapper-valid factors, and suppose every transition deletes
an exact minimum current-motif transversal.  Put `r_i=tau(F_i)`.  Corollary
2.2 gives

\[
 r_0\ge r_1\ge r_2\ge\cdots\ge0.
\tag{6.1}
\]

Thus the potential eventually stabilizes.  More positively:

* if every nonresident state admits an outgoing exact-minimum rethread with
  no seam-saturated plateau, residence is reached after at most `r_0`
  strict rounds;
* if every step has at most `(1-epsilon)r_i` active added seams, then

  \[
  r_{i+1}\le(1-\varepsilon)r_i,
  \tag{6.2}
  \]

  giving geometric convergence;
* if the potential stabilizes at a positive value and every recentered family
  is packing-perfect, then every plateau transition carries the full private
  packing of Theorem 4.1.

The exact obstruction is therefore no longer “new defects may appear.”  New
defects are harmless to monotonicity.  The obstruction is a positive
wrapper-valid sink or cycle in which every exact-minimum transition is
seam-saturated.

### 6.1 Completion-weighted Lyapunov functions

Ordinary `tau` is not always the correct radius inside a constrained state
space.  Let `W` be any class of equal-size degree-two factors on the fixed
physical vertex set.  Examples are:

* factors with both q1 palettes complete;
* factors with both q1 palettes complete and strict top biresidence; or
* factors satisfying an even larger protected wrapper.

For `F in W`, define the **completion-weighted motif radius**

\[
 \tau_{\mathfrak W}(F)=
 \min\bigl\{|F\setminus G|:
     G\in\mathfrak W,
     (F\setminus G)\cap M\ne\varnothing
       \text{ for every }M\in\mathcal H(F)
 \bigr\},
\tag{6.3}
\]

with value infinity if there is no such `G`.  The target `G` need not already
be resident; it must destroy every current motif and preserve the wrapper.

### Theorem 6.2 (wrapper-weighted monotonicity)

If `G in W` attains (6.3), then

\[
 \boxed{\tau_{\mathfrak W}(G)\le\tau_{\mathfrak W}(F).}
\tag{6.4}
\]

#### Proof

Put `D=F\setminus G` and `J=G\setminus F`.  Theorem 2.1 says `J` hits every
motif of `G`.  Deleting `J` from `G` and adding `D` returns the factor `F`,
which belongs to `W`.  Thus `J` is an admissible reverse cut in (6.3), and

\[
 \tau_{\mathfrak W}(G)\le|J|=|D|=\tau_{\mathfrak W}(F).
\]

QED.

This reversibility is the correct general meaning of a palette-weighted
descent potential.  It also shows why arbitrary static weights are unsafe:
weights can change after re-centering, and monotonicity need not survive.
Any cheaper admissible-cut relaxation may replace (6.3), but only if its cut
family is **reverse closed**: every allowed transition `F -> G` must make the
reverse added bank `J` admissible at `G`.

There is a natural hierarchy

\[
 \tau(F)\le\tau_{q1}(F)
 \le\tau_{q1+\mathrm{top}}(F)
 \le\tau_{\mathrm{full}}(F),
\tag{6.5}
\]

whenever the quantities are finite.  An irreplaceable palette row can make
the first inequality strict, exactly as in the base case below.

## 7. The certified first `k=16` transition

The source is

```
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
SHA-256 f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5
```

and the first re-centered state is the stored round-zero incumbent

```
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
SHA-256 d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8.
```

The enclosing two-round solver run has overall status `UNKNOWN` because its
second CEGAR round timed out.  This does not weaken the stored first-round
witness: an independent literal replay has status `PASS`.

### 7.1 Wrapper and exchange audit

Both factors have 858 selected quotient edge orbits.  Their exact exchange
is

\[
 |D|=|J|=147,
 \qquad |F_0\cap F_1|=711.
\tag{7.1}
\]

The sector histograms are

\[
 D:(76\ AA,8\ AB,63\ BB),
\tag{7.2}
\]

\[
 J:(73\ AA,14\ AB,60\ BB).
\tag{7.3}
\]

The final factor has both q1 supports `764`, strict top biresidence, three
quotient components, and five physical components of lengths

\[
 705,1890,3425,3425,3425.
\tag{7.4}
\]

It is not yet a connected carrier.  It has 2,205 physical positive short-run
violations, with length histogram

\[
 1^{150}2^{915}3^{1140}.
\tag{7.5}
\]

The deleted bank lies wholly in the old 476-edge packing union.  It hits all
226 old motifs: 220 once and six twice.  Because it also chooses exactly one
edge from each of the 147 disjoint packed motifs, it is a genuine minimum
old-motif transversal.

### 7.2 New exact min--max certificate

After re-centering at `F_1`, the 2,205 physical violations collapse to 147
distinct quotient motifs with size histogram

\[
 2^{10}3^{61}4^{76}.
\tag{7.6}
\]

Their edge union has size 390.  The overlap graph has 85 components with
motif-count histogram

\[
 1^{49}2^{24}3^6 4^3 5^1 6^1 9^1.
\tag{7.7}
\]

An explicit 97-motif edge-disjoint packing and an explicit 97-edge
transversal prove, by weak duality,

\[
 \boxed{\nu(F_1)=\tau(F_1)=97.}
\tag{7.8}
\]

The retained minimum transversal is entirely same-shore:

\[
 59\ AA+38\ BB,
\tag{7.9}
\]

and consists of 45 edges added in the first rethread plus 52 edges retained
from the source.

### 7.3 Exact transition potential

Every one of the 147 new motifs meets `J`, directly replaying Theorem 2.1.
Only 107 of the 147 added edges are active in any new motif.  Therefore

\[
 \tau(F_1)\le107,
\]

giving the first 40 units of descent.

The seam traces have occurrence histogram

\[
 1^{137}2^{10}.
\tag{7.10}
\]

There are 99 distinct singleton-locked seams.  After forcing them, only the
two pair constraints

\[
 \{6794,11729\},
 \qquad
 \{19526,22168\}
\tag{7.11}
\]

remain uncovered.  They need two further edges, so

\[
 \sigma(F_0,F_1)=101.
\tag{7.12}
\]

Finally the unrestricted motif transversal uses retained collars to reduce
101 to 97.  Substitution in (0.5) gives the exact ledger (0.6).

The six seam-coalescence units occur in overlap components

\[
 5,26,37,47,74,75,
\tag{7.13}
\]

and the four retained-edge captures occur in components

\[
 24,28,41,71.
\tag{7.14}
\]

The chosen retained capture edges are respectively

\[
 6932,\quad7714,\quad19329,\quad8058.
\tag{7.15}
\]

Thus the 50-unit drop is locally certified component by component; it is not
an inference from a global solver objective.

## 8. The genuine radius-97 re-centered face

The 97 packed new motifs have pairwise-disjoint union of 322 selected edge
orbits:

\[
 159\ AA+26\ AB+137\ BB.
\tag{8.1}
\]

Every exact radius-97 deletion set hitting the new family chooses exactly
one edge from every packed motif and no edge outside this union.  Those 322
edges touch 407 quotient vertices.  The full loopless catalogue contains
5,910 off-`F_1` seams on those vertices:

\[
 2724\ AA+746\ AB+2440\ BB.
\tag{8.2}
\]

This is materially smaller than the original radius-147 face, whose fixed
packing union had 476 edges, 586 endpoint vertices before all old motif
constraints, and 12,320 off-source seams on that endpoint atlas.

Therefore re-centering is not merely a change of objective wording.  It
produces a new exact finite master with a smaller forced cut union and a
different seam catalogue.  The original CEGAR keeps radius 147 measured
from `F_0`; a radius-97 solve around `F_1` is allowed to leave that original
sphere while preserving the monotonicity theorem.

### 8.1 The exact palette-weighted correction `97 -> 98`

The ordinary 97-edge face is nevertheless q1-impossible for a local,
solver-free reason.  Overlap component 5 consists of the two motifs

\[
 M_5=\{22511,22520\},
\tag{8.3}
\]

\[
 M_{66}=\{22511,22692,25634\}.
\tag{8.4}
\]

Their intersection is the singleton `{22511}`.  Hence their ordinary local
transversal number is one, attained uniquely by edge 22511.

In `F_1`, edge 22511 is the unique selected provider of upper-q1 colour

\[
 (1,1907).
\tag{8.5}
\]

The exact radius-97 packing-endpoint atlas contains no off-factor provider
of this colour.  The larger atlas exposed by **all** 390 current motif edges
also contains none.  Therefore every q1-complete exact-radius-97 rethread
must retain edge 22511; the same is true for any rethread whose cut endpoints
remain inside the full current-motif union.  A larger-radius cut outside that
union could expose a different provider and is not ruled out here.  Once
22511 is forbidden, (8.3)--(8.4) require two distinct cuts:

\[
 22520
 \quad\text{and one of}\quad
 22692,25634.
\tag{8.6}
\]

All other overlap components retain their ordinary optimum.  Since they
contribute 96, the exact constraint-weighted value is

\[
 \boxed{96+2=98.}
\tag{8.7}
\]

One explicit palette-safe transversal uses `22520,22692`; globally it has

\[
 59\ AA+39\ BB.
\tag{8.8}
\]

This proves two distinct statements.

1. No q1-complete exact-radius-97 rethread about `F_1` exists.  This is a
   direct structural certificate, stronger in proof scope than the recorded
   radius-97 solver infeasibility transcript.
2. The first cut radius not excluded by this palette lock is 98.  The
   explicit 98-edge set is a motif transversal and avoids the locked row,
   but it does **not** by itself prove degree, both q1 palettes, or top
   completion.

Thus

\[
 \tau_{q1}(F_1)\ge98,
\tag{8.9}
\]

while equality in the completion-weighted sense of (6.3) remains conditional
on finding an actual q1-complete radius-98 factor.  The exactly proved finite
quantity in (8.7) is the palette-lock relaxation
`widehat tau_pal=98`.

For the **internal lock-safe branch** at radius 98, the correct minimum cut
domain is no longer the 322-edge packed union.  It is the full 390-edge
current motif union, which touches 466 quotient vertices.  Its off-factor
loopless seam atlas has 7,761 edges:

\[
 3379\ AA+984\ AB+3398\ BB.
\tag{8.10}
\]

The affected component spends the one extra cut inside that full motif
union, so every internal lock-safe radius-98 cut is accounted for by this
componentwise domain.  A global radius-98 cut can instead delete `22511` and
spend its extra unit outside the motif union to expose a replacement provider;
Section 4 of the joint-surcharge report gives the complete two-tier
decomposition.

### 8.2 Exact overlap-component product normal form

The weighted 98-face has a much smaller discrete description than its
390 cut-edge variables suggest.

Let the motif-intersection components be

\[
 \mathcal H_1,\ldots,\mathcal H_s,
\]

and let `E_i` be the union of the motifs in `H_i`.  Distinct `E_i` are
disjoint by definition.  Put into component `i` every hard palette lock whose
support lies wholly in `E_i`.  Let `r_i` be the minimum size of a local
transversal obeying those locks, and let

\[
 \mathcal D_i={D_i\subseteq E_i:
   D_i\text{ is lock-safe, hits }\mathcal H_i,
   |D_i|=r_i\}.
\tag{8.11}
\]

### Theorem 8.1 (component-product theorem)

If all preimposed hard locks are component-local, then

\[
 \widehat\tau_{\rm pal}=\sum_{i=1}^s r_i,
\tag{8.12}
\]

and the complete family of minimum lock-safe transversals is exactly

\[
 \left\{\bigcup_{i=1}^s D_i:
       D_i\in\mathcal D_i\text{ for every }i\right\}.
\tag{8.13}
\]

#### Proof

Every global transversal restricts on `E_i` to a transversal of `H_i` and
must obey its local locks, so it has at least `r_i` edges in `E_i`.  The
supports `E_i` are disjoint, giving the lower bound (8.12).  Conversely, a
choice `D_i in D_i` for every component has disjoint union, obeys every local
lock, and hits every motif.  Equality forces equality in every component,
which gives the exact product (8.13).  QED.

For the present `F_1` family:

\[
 s=85,
 \qquad\sum_i r_i=98.
\tag{8.14}
\]

The total number of stored local options is only

\[
 \sum_i|\mathcal D_i|=262,
\tag{8.15}
\]

and

\[
 \max_i|\mathcal D_i|=8.
\tag{8.16}
\]

The exact domain-size histogram is

\[
 1^{10}2^{17}3^{31}4^{21}5^1 6^2 8^3.
\tag{8.17}
\]

Before the palette lock, the corresponding ordinary total is 261.  The
exceptional component replaces its sole ordinary option `{22511}` by the
two safe options

\[
 \{22520,22692\},
 \qquad
 \{22520,25634\},
\tag{8.18}
\]

which changes 261 to 262 while changing the summed cut size from 97 to 98.

### 8.3 Bounded-domain degree/q1 CSP

Theorem 8.1 gives an exact finite-domain master for the degree-plus-q1
completion relaxation.  Introduce one variable

\[
 z_i\in\mathcal D_i
\]

per overlap component and one Boolean `y_e` for each candidate added seam.
For a local option `alpha in D_i`, precompute

\[
 a_{i\alpha}(v)=d_{D_{i\alpha}}(v),
\tag{8.19}
\]

the number of deleted incidences at quotient vertex `v`, and

\[
 \ell_{i\alpha}(q)
 =|D_{i\alpha}\cap P_F(q)|,
\tag{8.20}
\]

the number of deleted current providers of q1 row `q`.

Then exact quotient degree restoration is

\[
 \sum_{e\ni v}y_e
 =\sum_i a_{i,z_i}(v)
 \qquad(v\in V),
\tag{8.21}
\]

and exact q1 support is

\[
 \mu_F(q)-\sum_i\ell_{i,z_i}(q)
 +\sum_{e\in P^+_F(q)}y_e\ge1
 \qquad(q\text{ a lower or upper row}).
\tag{8.22}
\]

Here `mu_F(q)` is the current provider multiplicity and `P_F^+(q)` is the
off-factor candidate provider bank.  Equations (8.21)--(8.22), together with
`z_i in D_i` and binary distinct-seam selection, are necessary and sufficient
for the degree-plus-both-q1 relaxation on this minimum weighted face.

Thus the local choices communicate only through endpoint-deficit and q1-row
signatures.  Options having the same pair of signatures may be merged
without changing this relaxation.  Equivalently, the seam subproblem may be
solved by the coloured factor/Hall--Tutte machinery and returned to the 85
finite-domain variables through Benders rows.

The exact current census is:

* 85 local variables with 262 stored options and maximum domain eight;
* 7,761 candidate seam variables;
* 858 endpoint degree rows; and
* 327 active lower plus 322 active upper q1 rows.

This theorem is conditional only on the stated component-local hard locks.
A palette constraint whose relevant current providers span several overlap
components belongs in the global q1 rows (8.22), not in one local domain.

Top biresidence is also **not** already contained in (8.21)--(8.22).  It adds
the boundary-matching and same-shore boundary-reach rows.  Newly created
motifs require lazy separation, while connectivity and voltage remain global
post-audits or subtour constraints.  Hence “coupled only through endpoint
degree/q1 rows” is exact for the degree/q1 completion layer, not for the
entire literal carrier theorem.

## 9. Precise remaining gate

The 85-domain internal radius-98 completion is now exactly infeasible already
at degree plus both q1 palettes, with top residence relaxed.  Degree alone
and each single-palette problem are feasible.  Therefore the internal hard
radius is at least 99, and the extra obstruction is a joint
endpoint-conditioned lower/upper palette rank defect.

This does not close global radius 98.  The exact tier identity shows that the
only omitted branch cuts `22511` at ordinary local minimum, takes one source
edge outside the 390-edge motif union, and exposes one of 14 crossing
providers on seven outside nodes.  There are 28 provider/exterior-cut portal
incidences.  The immediate gate is to close or realize those portal
submodels.  Only after a degree-plus-both-q1 completion exists do top path
lengths, new motifs, connectivity/voltage, deeper shadows, and the compiler
re-enter.

Ordinary monotonicity alone gives no strict second descent.  The global
completion-weighted potential of Theorem 6.2 remains the correct iterative
quantity; the source-centered 466-node atlas is not reverse closed and must
not itself be treated as a Lyapunov domain.

## 10. Frozen artifacts

Exact first-round factor and replay:

```
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
SHA-256 d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8

scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.audit.json
SHA-256 cf1f33dda9f018fb76d2d17f57f7c7df9edd37688803711bb90ffa9bbe6a6e11
```

Explicit new-family min--max certificate and replay:

```
scratch/k16_dynamic_cross_r147_round0_residence_tau97_20260729.certificate.json
SHA-256 6d6261267e9d2e9883b4afb2929b27ccbc8e005d4cd35fc068b628fefa414117

scratch/k16_dynamic_cross_r147_round0_residence_tau97_20260729.audit.json
SHA-256 e64dde93b7c24112247bc249e29ae584ad353c1a4a15b5e3636cb1372ff0d46d
```

Independent componentwise min--max table:

```
scratch/k16_dynamic_cross_r147_round0_motif_minmax_20260729.audit.json
SHA-256 e08ea84e60f4abb35295a5f832b619a42e4213efe274e390c18d2d5f273dcb38
```

Independent radius-97 palette-gate audit:

```
scratch/threadD_k16_recenter_r97_palette_gate_20260729.audit.json
SHA-256 84a42625ba498a75bf5f961263a161ace45557197a40ef7babc6be068126269e
```

New transition audit:

```
scratch/audit_k16_iterative_recentered_motif_descent_20260729.py
SHA-256 7921db4969beb02e6452f05570995cc3d39d403354d6ff025ba36e561ebfad04

scratch/k16_iterative_recentered_motif_descent_20260729.audit.json
SHA-256 116cab238acdfd2663014a4119bd3b5f962b28c92771b4f44c2e2b7d72648089
```

The transition audit performs no search.  It rebuilds both motif families,
checks the two packing/transversal certificates, verifies the exact edge
exchange and wrapper census, computes the seam traces, and localizes all ten
nontrivial descent components.  It also proves the exceptional two-motif
palette lock, the exact 98-edge lock-safe transversal, and the full-union
candidate census.  Finally it enumerates all 262 local safe-transversal
options and freezes the 85-variable product normal form.  No heavy local job
was run.
