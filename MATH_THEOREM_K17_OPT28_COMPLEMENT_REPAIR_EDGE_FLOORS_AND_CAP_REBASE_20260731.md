# The `K17` OPTIMAL28 complement needs at least 1,900 changed diamonds before common-cap Hall

Date: 2026-07-31  
Status: exact fixed-chronology obstruction, exact marked-preserving repair
lower bounds, and common-cap rebase; no repaired carrier or `K17` word is
claimed

## 0. Verdict

The connected OPTIMAL28 residual completion has solved topology and the
complete lower-`q1` palette.  Its literal owner cycle has all `24310`
rank-nine owners and all `24310` rank-eight intersections exactly once.  The
marked bank is one contiguous `4108`-owner path and is internally
residence-clean.

The induced two-bank depth-two row is nevertheless impossible:

```text
row length                                      24311
marked rank-nine rows                            4108
distinct direct rank-eight facets               20203
strict D2 bad runs                               2392
  length one / length two                   1025 / 1367
maximal-envelope empty letters                      0
failed replay rows                               3568
missing carrier bit incidences                   3759
upper holes at ranks 10 / 11 / 12       1900 / 911 / 128
upper holes at ranks 13,...,17                       0
conditional scalar lower slack                   3293.
```

Thus the current common-cap system is infeasible **before Hall**.  The
maximal envelope is already the largest possible physical word below this
row; intersecting it with target caps can only delete more bits and cannot
repair any of the `3759` missing carrier incidences.

Two exact lower bounds show that the live complement repair is macroscopic.
Keeping the marked path fixed and staying in the standard owner/facet
zipper:

\[
 \boxed{\tau_{\rm residence}=1603},                 \tag{0.1}
\]

where `tau` is the minimum number of old complement adjacencies which must
be deleted to hit every inherited length-two/three owner run, and

\[
 \boxed{|E_{\rm new}|\ge1900}                       \tag{0.2}
\]

because each of the `1900` absent rank-ten targets requires a new Johnson
adjacency with that union.  The same changed edges may serve both rows, so
the joint bound is `1900`, not `3503`.

The current residual-`b`-flow face is closed still more strongly.  It keeps
`724` bad owner runs wholly inside `257` complement components; `227`
length-three runs lie wholly inside `141` individual macro words.  No
reordering, reversal, or residual incidence rectangle on intact components
can repair them.  Interior occurrence/macro rethreading, or a genuinely
nonflat chronology, is mandatory.

After such a repair, the scalar common-cap ledger remains

\[
    45332\text{ residual targets on }48625\text{ short cells},
    \qquad \text{slack }3293,                        \tag{0.3}
\]

provided the marked path and exact lower palette remain fixed.  The ordered
facet rail, maximal envelopes, upper providers, and common-cap guards are
not invariant and must be rebuilt from the repaired chronology.

## 1. Exact two-bank materialization

Rotate the authenticated owner cycle at position `21331` and write it as

\[
 P_1,\ldots,P_a,Q_1,\ldots,Q_b,P_1,
 \qquad a=4108,\quad b=20202.                       \tag{1.1}
\]

The marked path begins with `0x118fa` and ends with `0x14736`; the complement
begins with `0x04776` and ends with `0x058fa`.  Define

\[
 F_0=P_a\cap Q_1,qquad
 F_i=Q_i\cap Q_{i+1}\ (1\le i<b),qquad
 F_b=Q_b\cap P_1,                                  \tag{1.2}
\]

and

\[
                    Z=P_1\cdots P_aF_0\cdots F_b.  \tag{1.3}
\]

Literal replay proves:

* the `F_i` are `20203` distinct rank-eight sets;
* the `4107` internal intersections of `P` are distinct and disjoint from
  the `F_i`;
* these two families partition the complete rank-eight layer; and
* adjacent unions in `Z` have rank profile `10^4107 9^20203`.

Thus topology, direct lower palette, and the scalar count (0.3) are exact.
They are not sufficient for physical inversion.

### Lemma 1.1 (facet erosion)

Let \(q_0,\ldots,q_{s-1}\) be an owner word and put
\(f_i=q_i\cap q_{i+1}\).  A strict coordinate run

\[
                         0\,1^r\,0                  \tag{1.4}
\]

in the owner word becomes the strict run

\[
                         0\,1^{r-1}\,0              \tag{1.5}
\]

in the facet word.

#### Proof

The coordinate belongs to `f_i` exactly when it belongs to both adjacent
owners.  Adjacent intersection erodes each strict positive run once at each
end and preserves its internal zero boundaries.  \(\square\)

The complement `Q` has `1025` strict internal runs of length two and `1367`
of length three.  Lemma 1.1 gives exactly the `1025` length-one and `1367`
length-two runs of `Z`.  Every maximal-envelope letter is nonempty, but
three-window erosion deletes those short runs and therefore fails to replay
`3568` rows.

A two-row certificate already suffices.  In coordinate zero the `Z` trace
at rows `4258,...,4261` is `0,1,1,0`; rows `4259,4260` are respectively
`0x1c325,0x18725`, while maximal replay gives `0x1c324,0x18724` and loses
bit zero.  Reversal and either bank-boundary opening retain the same `2392`
bad runs and `3568` failed rows.

### Corollary 1.2 (Hall is not reached)

No nonempty physical word has second derivative `Z`.  Consequently there is
no semantically valid common-cap matching instance on this fixed row.

#### Proof

Every realizing letter is contained in the maximal envelope.  Its replay is
therefore contained in the maximal replay, which already omits required
bits in `3568` rows.  Additional target caps only take further intersections.
\(\square\)

This is an inversion obstruction, not a Hall deficiency.

## 2. The exact residence hitting hypergraph

Index the old complement edges linearly.  For every strict coordinate run

\[
 Q_s,\ldots,Q_{s+r-1},\qquad r\in\{2,3\},          \tag{2.1}
\]

with zero-coordinate owners immediately before and after it, form the edge
interval

\[
                 H=[s-1,s+r-1].                     \tag{2.2}
\]

It consists of the entry edge, all internal run edges, and the exit edge.
Let \(\mathcal H\) be the resulting family of `2392` intervals.

### Lemma 2.1 (every inherited defect must be cut)

Any marked-preserving owner rethread whose complement facet rail has no
strict run shorter than three must delete at least one old edge from every
\(H\in\mathcal H\).

#### Proof

If all edges of `H` survive, every internal vertex of that old path segment
already has its two selected incident edges.  Degree two forces the whole
segment to remain consecutive in the new cycle, possibly reversed.  Its
coordinate trace is still `0 1^r 0`, and Lemma 1.1 leaves a strict facet run
of length `r-1<3`.  \(\square\)

### Theorem 2.2 (exact interval transversal)

For the authenticated complement,

\[
             \tau(\mathcal H)=\nu(\mathcal H)=1603. \tag{2.3}
\]

Here \(\tau\) is the minimum edge stabbing set and \(\nu\) the maximum number of
pairwise-disjoint support intervals.

#### Proof

Sort the intervals by increasing right endpoint.  Repeatedly select the
right endpoint of the first interval not yet hit.  The resulting `1603`
points hit all `2392` intervals.  The `1603` intervals which triggered those
choices are pairwise disjoint, so any hitting set has at least `1603`
points.  This is the usual exact packing--cover proof for intervals.  The
frozen audit records both checks and hashes the disjoint trigger list.
\(\square\)

If only owner minimum run three were required, the `1025` length-two runs
alone have transversal number `754`.  The two-bank facet rail needs owner
minimum run four, so (2.3), not `754`, is the relevant number.

## 3. The stronger rank-ten edge floor

For a Johnson edge `e={A,B}` on rank-nine owners, write

\[
             \ell(e)=A\cap B,\qquad u(e)=A\cup B.   \tag{3.1}
\]

### Lemma 3.1 (rank-ten intervals are edge-labelled)

If a nontrivial interval of rank-nine Johnson owners has union `S` of rank
ten, then every adjacent edge in that interval has upper label `S`.

#### Proof

Every owner in the interval is a rank-nine subset of `S`.  Two adjacent
distinct Johnson owners have rank-ten union contained in `S`; equal ranks
force that union to be `S`.  \(\square\)

### Theorem 3.2 (1,900 changed-diamond floor)

Every marked-preserving, lower-`q1`-exact owner rethread which supplies all
rank-ten targets through its owner chronology selects at least `1900` edges
not present in the authenticated cycle.

#### Proof

The current cycle has exactly `1900` absent rank-ten labels.  By Lemma 3.1,
each one requires a selected edge with that upper label.  No old selected
edge has any of those labels, and one edge has only one upper label.  Thus at
least `1900` newly selected edges are necessary.  \(\square\)

Since the repaired factor has the same number of edges, at least `1900` old
edges are deleted as well.  At equality, every new edge must supply a
different old hole, and every removed edge must leave its old upper target
with another provider.  The deletion set may simultaneously hit all
residence intervals in Section 2; only the maximum

\[
                         \max(1603,1900)=1900        \tag{3.2}
\]

is forced.

Theorem 3.2 is architectural: a genuinely nonflat compiler which witnesses
rank-ten targets outside the rank-nine owner chronology can escape it.

## 4. Exact marked-preserving repair variables

Let \(C_P\) be the `4107` lower colours on the fixed marked path, let
\(\mathcal V_8=\binom{[17]}8\), and put

\[
             \mathcal F=\mathcal V_8\setminus C_P,
             \qquad |\mathcal F|=20203.             \tag{4.1}
\]

For \(F\in\mathcal F\) and every rank-ten set \(S\supseteq F\), with
\(S\setminus F=\{a,b\}\), there is a unique Johnson diamond

\[
             e(F,S)=\{F\cup\{a\},F\cup\{b\}\}.      \tag{4.2}
\]

Use a binary variable `z_(F,S)`.  A marked-preserving lower-rainbow
Hamilton cycle is exactly a selection satisfying:

\[
             \sum_{S\supset F}z_{F,S}=1
             \qquad(F\in\mathcal F),                \tag{4.3}
\]

degree two at every complement owner, degree one at each marked endpoint,
degree zero at every other marked owner, and the ordinary two-factor
connectivity cuts.  Adding the fixed marked path then gives one Hamilton
cycle.  The upper rank-ten rows are linear:

\[
 m_P(S)+\sum_{F\subset S}z_{F,S}\ge1
             \qquad\left(S\in{[17]\choose10}\right), \tag{4.4}
\]

where `m_P(S)` is the number of fixed marked edges with union `S`.

The difference of any two feasible lower-colour/degree selections is an
integer kernel vector and decomposes into incidence-alternating circuits.
Circuit toggles preserve owners and lower colours.  Connectivity, residence,
and the upper rows still require their own constraints.

Residence is imposed exactly by forbidding every selected complement path

\[
 V_0,V_1,\ldots,V_{r+1},qquad
 x\notin V_0,V_{r+1},\quad x\in V_1,\ldots,V_r,
 \quad r\in\{2,3\}.                                  \tag{4.5}
\]

Equivalently, use the per-coordinate run automaton `0,1,2,3+` and replay the
two marked/complement collars.  For ranks eleven and twelve, require an
explicit selected path inside `binom(S,9)` whose vertex union is `S`, or use
the exact accumulated-union path automaton.  Ranks thirteen through
seventeen presently have no holes, but a repair must retain one certified
provider for each target or pass full final replay.

Equations (4.3)--(4.5), the upper path-provider rows, and connectivity are
the smallest exact marked-preserving repair master.  The existing
component-pairing model is a strict subface and is empty by Section 5.

## 5. Why another residual `b`-flow cannot work

The exact component audit finds `724` owner runs of lengths two or three
wholly inside `257` immutable complement components.  Reversal and component
reordering preserve them.  Even after cutting at every exposed old-coordinate
port, `227` length-three runs remain wholly inside `141` individual
`A/X/Y` macro words.  Lemma 1.1 turns each into a forbidden length-two facet
run.

### Corollary 5.1 (fixed-skeleton no-go)

No residual owner-to-port pairing, connected or disconnected, can repair
the two-bank residence condition while those macro interiors are fixed.

Thus the new connected completion is the correct topology certificate, but
not a repair search space.  At least one of the following must occur:

1. an occurrence/matching rethread changes macro interiors;
2. bad macro material is moved into a modified marked bank with an exact
   slot/current ledger; or
3. a genuinely nonflat actuator avoids lowering that material into one
   facet rail.

## 6. Exact common-cap handoff after repair

Every solution of (4.3) keeps the marked owner count `4108` and the direct
facet **set** \(\mathcal F\).  Therefore it preserves the residual target set
and scalar ledger (0.3).  It does not preserve the ordered facet word.
Indeed consecutive facets determine the complement owners by

\[
                         Q_j=F_{j-1}\cup F_j.        \tag{6.1}
\]

Any nontrivial rethread changes the order, hence generally changes maximal
envelopes, candidate cells, and common-cap hosts.

A repaired candidate reaches the lower compiler only after it exports:

1. the literal ordered complement path and facet rail;
2. exact maximal-envelope nonemptiness and replay at every row;
3. complete upper-provider replay through rank seventeen;
4. all socket/prepin short cells and their distinct discharged targets;
5. the signed port/current and bank-interface collars; and
6. either common permanent bits and row/target hosts, or the complete
   rank-at-most-three bad-pair/bad-triple system.

Once rows 1--5 are frozen, the exact common-cap instance has `45332`
residual targets and `48625` singleton/pair cells.  Ordinary Hopcroft--Karp
Hall is only necessary.  It becomes sufficient on the permanent-bit/host
guarded face; otherwise the exact unary/pair/triple cuts are required.

## 7. Authentication and scope

Primary connected factor and literal zipper:

```text
scratch/k17_opt28_connected_owner_cycle_20260731.word
  SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa
scratch/k17_opt28_two_bank_d2_row_20260731.word
  SHA-256 a6ca69d2193bdd0c715687f8c9a971fb04fd2f2a9ab9ce2431baaa7063065930
scratch/ad_k17_opt28_twobank_d2_row_20260731.zrow
  SHA-256 18675acb0083aa7fea8e1505f871cc70b23a9261e6f59662cb9df87ca703a211
scratch/ad_k17_opt28_twobank_d2_row_20260731.audit.json
  SHA-256 81f0e403367ee0e32c0ac63404cebd2e87a3a2a9602475b01b3a3927c4c9cf20
  payload 591ef216c6c4d818e604ccad9d149ab6ab66c0fa6a124a3d8bc5382c2185726d
scratch/r_k17_opt28_onecycle_deep_common_cuts_20260731.audit.json
  SHA-256 a4e8b1a1c2b2cff2a851f6bd4d34046c9acbae5d8c45b9be8a2992e8c2572bd2
  payload e5accce62989199b398c8cdd5752f44a03df329a30f84c94dcfa9813dcfc4d3b
```

New exact interval/upper-edge lower-bound audit:

```text
scratch/audit_k17_opt28_complement_repair_floors_20260731.py
  SHA-256 8b301755ef697a0ce52f7115760a34a1ecb741974dedc507ec1dca33f7ce827a
scratch/k17_opt28_complement_repair_floors_20260731.audit.json
  SHA-256 9be467d5a1feca78ca5e361e49ab57ae3bda7bef32232aaa85c0ee8042102068
  payload 01a30120a9a0c05acaccab862e673bababe038086c0dfd79a5bfd76efe876cc7
```

The `1603` floor assumes the fixed marked path and the standard owner/facet
zipper.  The `1900` floor assumes rank-ten targets are supplied through the
rank-nine owner chronology.  Neither is a global obstruction to a genuinely
nonflat compiler.  No common-cap Hall verdict is claimed for any repaired
chronology, and no `K17` word follows.
