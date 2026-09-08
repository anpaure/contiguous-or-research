# AD audit: ghost-free K16 radius two and the waste21 safe-gap closure

Date: 2026-07-30

Status: the global two-substitution fibre is closed by an exact finite
certificate.  The arbitrary-cardinality waste21 collar is reduced to one
exact SAT instance; two bounded presentations of that instance ended
`UNKNOWN`.  Neither statement is a lower bound for a different length-12,873
word.

## 1. Frozen source and conventions

Let

```text
P = scratch/k16_ghostfree_parent_braid_best4_20260730.word
```

with zero-based positions.  Its SHA-256 is

```text
55b029e30954391d78308412139726bdbf4ebd65b655d79a511f14e1edf24caf.
```

An independent literal replay gives length `12873`, coverage `65531`, and
exactly the four holes

```text
H = {0xc879,0xce61,0xce63,0xe879}
  = {51321,52833,52835,59513}.
```

Every word cell is required to be a nonzero 16-bit mask.  A substitution
means that the final value differs from the incumbent value.  Two
substitutions are at distinct positions; two successive writes at one
position are just one final substitution and belong to the one-substitution
case.

The common part of the four holes is

```text
C = intersection(H) = 0xc861 = 51297,
```

and has six bits.  Consequently the elementary one-substitution scan has
exactly

```text
12873 (positions) * 63 (nonzero submasks of C) = 810999
```

rows.  It returned zero installers.  The stronger result below subsumes that
scan.

## 2. A complete two-substitution dichotomy

For a word `X`, a target `t`, and a position `q`, write
`K_X(q,t)` for the OR of the maximal consecutive `t`-compatible cells on the
two sides of `q`, excluding `q` itself.  A cell is `t`-compatible when it is a
submask of `t`.

### Lemma 2.1 (one-site witness or all-joint witness)

Suppose changing distinct positions `p,q` of `P` to nonzero values `u,v`
produces a universal word.  Exactly one of the following exhaustive cases
holds.

1. Some final witness of some `h in H` contains exactly one of `p,q`.
   Then the corresponding single substitution by itself creates `h` in
   `P`.
2. Every final witness of every `h in H` contains both `p` and `q`.

#### Proof

Every final witness of an old hole contains at least one changed position,
because an interval avoiding both changes is unchanged and therefore could
not have OR equal to an old hole.  If one such witness contains exactly one
change, the same interval is present with the other position restored, which
proves case 1.  Otherwise every witness of every old hole contains both
changes, which is case 2.  The alternatives are disjoint by definition.  

### Lemma 2.2 (exact second-site interval test)

Fix a genuine first substitution `(p,u)` which creates at least one old hole,
and let `D(p,u)` be the exact set of masks absent after this first
substitution.  Put

```text
U(p,u) = intersection_{d in D(p,u)} d.
```

If a second substitution `(q,v)` completes the word, then

```text
0 != v subseteq U(p,u)
```

and, with `X=P[p:=u]`,

```text
L(q;p,u) := union_{d in D(p,u)} (d \ K_X(q,d)) subseteq v.
```

Conversely, for a fixed `q`, every nonzero `v` satisfying

```text
L(q;p,u) subseteq v subseteq U(p,u)
```

creates at least one witness for every member of `D(p,u)`.  It remains only
to test whether the second substitution destroys a previously surviving
target.

#### Proof

Every `d in D(p,u)` is absent before the second change, so every new
`d`-witness contains `q`.  Its value at `q` is a submask of `d`; intersecting
over `d` gives `v subseteq U`.  All bits of `d` absent from the maximal
compatible context around `q` must be supplied by `v`, giving the lower
bound.  Conversely, `v subseteq d` and
`d\K_X(q,d) subseteq v` imply

```text
K_X(q,d) OR v = d.
```

The maximal compatible interval at `q` is therefore a literal `d`-witness.

### Lemma 2.3 (complete provider-first finite certificate)

For the frozen source `P`, there are exactly `151827` genuine first
substitutions which individually supply an old hole.  Of these, `147887`
have nonempty `U(p,u)`.  For none of those `147887` substitutions is there a
distinct position `q` with

```text
L(q;p,u) subseteq U(p,u).
```

Hence case 1 of Lemma 2.1 is impossible.

#### Certificate and audit

The primary implementation derives the exact post-first-edit debt set by a
sparse signed interval-multiplicity delta.  A second implementation derives
the same debt set from the intersection of all old witnesses of each target.
The two implementations agree on all decisive counts:

```text
source positions scanned/claimed       12873
provider substitutions                151827
nonempty debt intersections           147887
source seed-position visits          5591474
augmented candidate-position visits   371830
feasible common second positions           0
private witness-core targets           51323
private witness-core incidences        167283
maximum private core length                 8
```

The candidate-position compression is exact.  For a selected debt `d`, the
predicate

```text
d\U subseteq K_P(q,d)
```

is cached for all source positions.  Changing `p` can alter this predicate
only for `q` in the union of the old and new `d`-compatible components
incident with `p`, together with their boundary cells.  Both implementations
add exactly that union and then evaluate every debt at every retained `q`.
Thus zero retained `q` is an obstruction before any value enumeration, not a
heuristic provider cap.

### Lemma 2.4 (all-joint obstruction)

Assume case 2 of Lemma 2.1 and order the changed positions as `p<q`.  Then

```text
u subseteq C,
v subseteq C,
P_i subseteq C for every p<i<q.
```

For a hole `h`, let `J_h(p,q)` be the OR of the strict interior and of the
maximal `h`-compatible extensions immediately left of `p` and right of `q`.
Necessarily

```text
R(p,q) := union_{h in H} (h \ J_h(p,q)) subseteq u OR v subseteq C.   (2.1)
```

There are exactly `12935` pairs `(p,q)` whose strict interior is a submask of
`C`.  Exact enumeration gives

```text
min_{these pairs} popcount(R(p,q) \ C) = 2.
```

Therefore (2.1) fails for every possible support, so case 2 is impossible.

#### Proof

A joint `h`-witness contains `p,q`; every one of its cells, including `u,v`
and the fixed strict interior, is a submask of `h`.  Intersecting over the
four holes yields the three displayed submask conditions.  Extending a joint
witness maximally through `h`-compatible fixed cells does not change an OR
already equal to `h`.  Hence `u OR v` must supply every bit in
`h\J_h(p,q)`, proving (2.1).  The final numerical statement is an exact scan
of the `12935` possible supports.  It rejects every support before replacement
values are considered.

### Theorem 2.5 (global radius-two no-go for the frozen source)

No word obtained from `P` by changing at most two final positions to arbitrary
nonzero 16-bit values is universal.

#### Proof

The unchanged source is not universal.  A one-change completion belongs to
the provider-first enumeration and was not found.  For two distinct changes,
Lemma 2.1 is exhaustive.  Lemma 2.3 excludes its first case and Lemma 2.4 its
second case.

This theorem is global over all `12873` positions of this source.  It is not
a no-go for another length-12,873 word and says nothing about three or more
changed positions.

## 3. The actual waste collar and its safe gaps

Define four editable blocks

```text
A = [6433,6443]       size 11
B = [11727,11729]     size  3
C' = [12827,12829]    size  3
D = [12869,12872]     size  4
```

and let `S=A union B union C' union D`, so `|S|=21`.  These blocks contain the
seam waste, the two occurrences of the `0xc279` ghost, and the tail waste.
The exact support file is

```text
scratch/ad_k16_ghostfree_best4_waste21_positions_20260730.txt
SHA-256 c8a8a351dcb929a9654e7be6d89e37fc3cc0b85586e496b8d70e2a0736fc5de5.
```

The three fixed gaps have full OR:

```text
OR(P[6444..11726])  = 0xffff,
OR(P[11730..12826]) = 0xffff,
OR(P[12830..12868]) = 0xffff.
```

### Lemma 3.1 (safe-gap locality)

After arbitrary substitutions on `S`, every interval whose OR is a proper
mask intersects editable positions from at most one of `A,B,C',D`.

#### Proof

An interval meeting two different editable blocks contains the entire fixed
gap between two consecutive blocks.  That gap already has OR `0xffff`, so
the interval OR is `0xffff`, independently of all editable values.

Thus every proper-target witness is either wholly fixed or belongs to one of
the four blocks.  This is a literal interval statement; it does not discard
cross-boundary witnesses.  Such witnesses are simply forced to the full mask.

### Theorem 3.2 (exact four-chart union factorization)

Let `F` be the targets having a witness interval disjoint from `S`.  For a
choice `y_j` of the values in one block `j in {A,B,C',D}`, let
`Gamma_j(y_j)` be the targets witnessed by intervals whose editable-position
intersection is a nonempty interval contained in block `j`.  Then an
assignment `y=(y_A,y_B,y_C',y_D)` to the collar is universal if and only if

```text
F union Gamma_A(y_A) union Gamma_B(y_B)
  union Gamma_C'(y_C') union Gamma_D(y_D)
    = {1,...,65535}.                                      (3.1)
```

Each `Gamma_j` depends only on the values in its own block.  Thus the only
cross-block coupling in this fibre is the set-union requirement (3.1); no
literal witness uses variables from two blocks.

#### Proof

Every interval either avoids `S`, meets one editable block, or meets at least
two.  The first two cases give respectively `F` and one `Gamma_j`.  By Lemma
3.1, the third case has OR `0xffff`.  The full mask already lies in `F`, since
each displayed fixed barrier is itself a fixed full-OR interval.  This proves
both directions of (3.1) and the claimed dependence.

### Corollary 3.3 (exact 256-way source-hole owner cover)

None of the four source holes lies in `F`.  For each map

```text
sigma : H -> {A,B,C',D},
```

form a subinstance by requiring, for every `h in H`, at least one mapped
`h`-witness in block `sigma(h)`.  There are exactly `4^4=256` such
subinstances, and the unbounded collar formula is satisfiable if and only if
at least one of them is satisfiable.

#### Proof

Every satisfying assignment covers each old hole in at least one block by
Theorem 3.2; choosing one such block for each hole gives a map `sigma` whose
subinstance it satisfies.  The reverse implication is immediate because a
subinstance only adds requirements to the exact parent formula.

This is an exact, generally overlapping cover.  It is not a disjoint
partition: forbidding an auxiliary witness variable does not forbid the
corresponding interval from incidentally having the target OR.  A disjoint
least-owner version must forbid the underlying interval equalities in all
earlier blocks, not merely set their optional witness variables false.

The exact owner catalogue records all 16 block clauses and all 256 maps.  For
each of the four holes the block-clause sizes are `[66,6,6,10]`, their
variable sets are pairwise disjoint, and their union is exactly the parent's
88 witnesses.  No solver was invoked for this preparation:

```text
catalogue
  86b45dfe500680e8b801c4228887289af92cf84c672a3236a60a3938833168e7
  payload 5a432aa7893ee4e28ae16079d95d47da9b031fcb03e6554b3ac7d3e8cdb8e821
independent audit
  6a23e539a84f9b37e02b19621b0d083310df90345b4afa16d64cb6e616d299d5
branch appender
  8c235451027e4c44e352baed291f32ed1e11693b12ebdd911837df663156758c
runbook
  d633a4ccf7736c93c11eaa1b76e1e89cdfc5de5eb52efc4039a9860755813ac7
checksum ledger
  7aff88467f1f2554671c345a3c2b56cb05a82dcd5026586235ad9ecd012046ab
```

Each emitted branch has the same 9,157 variables and exactly 315,011
clauses.  Solving all 256 branches UNSAT would close the parent; one SAT branch
would still require the ordinary gauge/decode/full-replay chain.

## 4. Exact two-edit CNF as an independent regression

Although Theorem 2.5 makes a new solve unnecessary, an independent exact CNF
was emitted for exactly two genuine changes on `S`.  It has

```text
fixed-run-covered targets  65435
repair targets                100
value variables               336
change variables               21
prefix-counter variables       60
witness variables            8800
total variables              9217
clauses                    315225
literals                   826124
```

Every repair target has exactly

```text
C(12,2)+C(4,2)+C(4,2)+C(5,2) = 66+6+6+10 = 88
```

block-local interval terms.  There are no cross-gap proper-mask terms.  The
change variables are equivalent to bitwise inequality with the incumbent,
and the equivalence-complete prefix counter asserts exactly two changes.
Because Theorem 2.5 also excludes zero and one changes, this exact-two model
is equisatisfiable for universal completion with the radius-at-most-two model
within `S`.  Their raw assignment sets are not equal: the latter also contains
zero- and one-change rows, but none of those rows is a completion.

The audited frozen model hashes are

```text
CNF    d206783401181c560490ff75300e35c7ae20039b49ae557c4a69d0dc098fab51
map    244b6a8fbd7db13e1bae0e55c0ee2e16e97cdcd8e85986866181cbb0f1cfd7d6
stats  3d362a2426b695539b58b5e76e7c1023b357c47db067371c677d5647d48addaa
audit  3702a48ef4705ec9054b058c21f9076905b37e0cf014a82b3e2fc3f8a02ef8f3
```

The `210` position-pair fibres split exactly into `67` same-block pairs and
`143` cross-block pairs.  Same-block fibres retain genuine two-edit interval
terms.  Cross-block fibres are unions of two one-site provider signatures.
This partition is a strengthening and is not part of the completeness
argument for Theorem 2.5.

## 5. Arbitrary-cardinality safe-gap closure model

Remove the cardinality counter while retaining all 21 nonzero arbitrary
values and all literal interval-witness clauses.  By Lemma 3.1 this is an
exact model for the complete fixed-support fibre

```text
{ X : X_i=P_i off S, and 0<X_i<2^16 on S }.
```

It is not a bounded-radius model and it permits any number from zero through
21 of the collar values to differ from the source.  It was emitted on H100
under

```text
/home/amodo/or15/work/ad_ghostfree_best4_collar21_unbounded_20260730_990eea44
```

without invoking a solver.  Its independently reconstructed exact size is

```text
variables   9157
clauses   315007
literals  825557.
```

The model was reconstructed clause-for-clause from the source word and support
rather than accepted from emitter metadata.  All 8,800 witness ranges were
also checked to lie in one block.  The frozen hashes are

```text
CNF    d4c59bd85ed8d34b05186348a628e42dcd751d2f42b904d3031d298b99f225a3
map    cda02c8773de2079f52f1aeae6e7fa3b6978d12ac5cbaca5a1cd0d5bc13db99f
stats  ab0f217b9e5986164c10b253951ae4715c03caaa434bf65d466f5bc500305e98
audit  dcaee062ee8f096de91f9df88ca2a0f3a8648d11e006b2bf2eb44dde7d6c43fa
audit payload
       55bd9ecaeabb42a005a1fbd3362d4a4c728d63d22eba31389311ee531d459526
independent audit source
       990eea4406224f908cc4d343ffc38df7898ee7515837dd2b5057b197878b0614
```

### Proposition 5.1 (exact unbounded presolve)

In the unbounded model, each of the 21 change indicators occurs only in its
17-clause equivalence definition.  It occurs in no witness or target clause.
For every assignment of the value bits there is exactly one extension to the
change indicator.  Existentially eliminating those 21 indicators and their
`21*17=357` defining clauses therefore preserves exactly the same value
assignments.  After dense renumbering the exact reduced dimensions are

```text
variables   9136
clauses   314650
literals  824528.
```

Indeed each eliminated definition contributes `16*2+17=49` literals, so the
literal count falls by `21*49=1029`.  This is a sound model-size reduction;
it is not a restriction on the number of changed values.  The first frozen run
uses the fully audited unreduced formula so that any proof can be checked
against its authenticated CNF without a further composition map.

One proof-retaining run was launched at `2026-07-30T09:53:36+00:00` on H100
CPU 11, with a 1,800-second wall cap, a 4 GiB address-space cap, and one CPU
worker.  The launch wrapper has SHA-256

```text
0e6dfe06480ebe87fb51f8532406fa4dbbbdc8ce104e2608bfe3e32af7e7f4e6.
```

The run ended at `2026-07-30T10:23:26+00:00` after 1,790.01 seconds with
solver exit code zero and exact status `s UNKNOWN`.  Maximum RSS was 147,360
KiB.  Its 2,968,154,241-byte partial DRAT stream has SHA-256

```text
a58201ae66fadeb755e211262a2c85c2337ea3b2873ddd7e4908344b696070db.
```

That partial stream is not a proof and was not checked as one.  The harvested
run audit is

```text
scratch/ad_k16_ghostfree_best4_collar21_unbounded_raw_s2111721_20260730/run.audit.json
SHA-256 a843a360651ca40633054ebebf88d323024afe282a9e5d63dbb250aa34cfe868.
proof-size record
  bb88005c1b63e010696c6967d58a5a8da0b0cd5fc2844aa92b3133cd304cc9f7.
```

Thus this run establishes neither SAT nor UNSAT.

### Proposition 5.2 (incumbent-gauge phase isomorphism)

Complement each mapped value-bit variable exactly when the corresponding bit
of its frozen source cell is one, leaving change and witness variables
unchanged.  This literal-sign involution is a bijection between models of the
base CNF and models of the transformed CNF.  It flips 102 of the 336 value-bit
variables, preserves all dimensions, and makes the all-false value-bit phase
decode to the frozen incumbent collar.

The exact transformed package is

```text
scratch/ad_k16_ghostfree_best4_collar21_incumbentflip_20260730/
phase CNF
  99afc694da1e1376a618412c558aee6b95d1fff0c17b7e4402babdaad5ba0a13
manifest
  a7e06f49a472508e617a044a4fbd880b8a0b2df7091d7889c744058e74653621
independent clause/involution audit
  27b427e2c1367fab943f002b8470c323d00dd96685d887ce2ac7382c166d7215
fail-closed total-model unflipper
  b3af100760db68beec781a21b51b266cb58824f67912ba01756eb2984b16ca7a
independent unflipper regression audit
  ab4cdb12b0bfec6d1d4c95213661b6bd0f7d7922ececafe9e2d210c43d4131bb
```

The independent audit compares all 315,007 clauses sign by sign and applies
the transform twice to recover the authenticated base formula.  Any SAT model
must be unflipped to the original variable convention before the pinned
decoder and the two complete 65,535-mask replays are applied.  The transformed
formula is not a restriction and cannot turn an UNKNOWN result into an UNSAT
claim; it is a solver-phase normalization only.

Exactly one incumbent-gauge run was launched at
`2026-07-30T10:29:56+00:00` on H100 CPU 31, with one worker, a 1,800-second
outer wall cap, a 1,790-second Kissat cap, and a 4 GiB address-space cap.  Its
runner has SHA-256

```text
3d0f9514564eafb318e19827c83e214f83bcbe37400f36f52229919f65571573.
```

The command forces the solver's decision phase false with
`--phase=false --forcephase=true` and uses SAT bias.  This is a branching
heuristic, not a unit assignment or a restriction of the model.  Until a
model passes the unflip and both literal replays, or an UNSAT proof passes both
DRAT and LRAT checking, no terminal claim is permitted.

The run ended at `2026-07-30T10:59:46+00:00` with solver exit code zero and
the exact status line `s UNKNOWN`.  Its measured wall time was `1790.02`
seconds, solver process time was `1777.03` seconds, and maximum RSS was
`149120` KiB.  The emitted `3560565485`-byte partial DRAT stream has SHA-256

```text
998b1c8491ec71f50829bab856e9ba34fb2b09b4475882a095e410dd5d61251c.
```

That stream is not a proof and was not checked as one.  The harvested run
audit is

```text
scratch/ad_k16_ghostfree_best4_collar21_incumbentflip_20260730/run.phase.audit.json
SHA-256 a82d1e9b0da75a7ba0869d01bdafbdbb296dc7beba3b3b96fa7adf2341e14733.
```

Thus the incumbent-gauge run, like the raw run, establishes neither SAT nor
UNSAT.  The two runs are presentations of isomorphic formulas and are not two
independent mathematical instances.

### Proposition 5.3 (exact radius-two presolve for Collar21)

Let `c_1,...,c_21` be the model's positive change indicators.  For every
two-element subset `T` of these indicators, append the clause

```text
OR_{c notin T} c.                                           (5.1)
```

The resulting 210-clause extension has exactly the same satisfying
assignments as the unbounded Collar21 completion formula.  It has no new
variables and adds exactly `210*19=3990` literals, for totals of 9,157
variables, 315,217 clauses, and 829,547 literals.

#### Proof

All clauses (5.1) hold if and only if at least three change indicators are
true.  Indeed, if at most two are true, extend their set to a two-element
`T`; the associated clause is false.  If at least three are true, every
two-element `T` omits a true indicator, so its clause is true.  By Theorem
2.5, no universal assignment of the frozen source has at most two changed
positions.  Every satisfying assignment of the parent CNF already encodes a
universal completion and has the exact change indicators, so it satisfies
all of (5.1).  Conversely every model of the extension is a model of its
parent.  Hence the two satisfying-assignment sets are equal.  The extension
only cuts ambient value/change rows which were never models of the complete
parent CNF.

The clauses were emitted identically in the base and incumbent-gauge
presentations.  An independent parser verified the original clause prefix,
all 210 omitted pairs, all 19-literal tails, both headers, and both hashes;
no solver was invoked.  A future UNSAT proof checked against a strengthened
CNF must be composed with Theorem 2.5 to conclude UNSAT of the original CNF;
the DRAT/LRAT file alone would certify only the strengthened presentation:

```text
base strengthened CNF
  db00c11d4d77340e771c8f640cbcb3aceb4afe7efde1dabc5ac5ba79ef04dd61
phase strengthened CNF
  936ae76f4a6ae4c35686ff15723eec18d93a618b2b259044446d11c7332013c1
manifest
  5282e4255a7549bba0ed033c9c2ba286377282e56c6cf4dcbc1e68ba4bb7f87b
independent audit
  d34b608a291ed8aebb6da8f0b547293e1f68756aba9488dd47374d28808d1543
```

## 6. Authenticated radius-two artifacts

```text
scratch/search_k16_provider_first_seeded_exact_20260730.cpp
  ee0623fdf3b2ba5cbb230bbef97c6809eeb128949a690472970f17b8579e2468
scratch/search_k16_exact_two_edit_multihole_20260730.cpp
  e552c848a52c275a09105cccda888804e9404020b4fe856269a28e377c3e564c
scratch/audit_k16_ghostfree_best4_provider_core_independent_20260730.cpp
  70cf6737f1cc3e5cbf0b54d8799ffe11eb634b7d29fdd9f8943692db8214dc4c
scratch/search_k16_exact_joint_two_edit_multihole_20260730.cpp
  aded0eecdc8e62dec044c4c05752a23c2c64c1fb1e93711fe776b2ec2f4bbff3
scratch/k16_ghostfree_best4_radius2_exact_20260730/ghostfree_provider.audit.json
  b33a3c26bc867b6392dc10bcc107939fc5e94050ba22601625a1519307853665
scratch/k16_ghostfree_best4_radius2_exact_20260730/ghostfree_provider_one.audit.json
  565b7ee90576bd220bfeb708962e49a5748aa2fc671b82e7804fc80be57c5594
scratch/k16_ghostfree_best4_radius2_exact_20260730/ghostfree_provider_core_independent.audit.json
  17ad37b3fa954463b9ad79eae73e926dd09a1c8552e0d196ead60153df5afec0
scratch/k16_ghostfree_best4_radius2_exact_20260730/ghostfree_joint.audit.json
  8185847d811822a73d9ee3a882582bc6ea202acad48373b81420e251c3d45d11
scratch/audit_k16_ghostfree_best4_radius2_exact_20260730.py
  4c86e60603e23f390254081ffa98c9c49fdbffabde8e5df928e8f71103793d8d
scratch/k16_ghostfree_best4_radius2_exact_20260730/audit.composed.json
  39ee78b4a9465923e8f9e64fdffbf5a81605d2cdcbe41542fa86dd8c1e73a304
  payload af57b0e6438f1e11252ac5991a0ccbd2700b90f8d1c260669f36983b866843c2
```

The exact radius-two conclusion is an enumerative certificate with two
independent provider-first implementations and an independently reconstructed
all-joint obstruction.  It is not a DRAT proof of the unbounded collar CNF.
The composed JSON authenticates the provider wrapper but does not itself list
the wrapper's included dependency displayed above, nor its own composition
script.  Both hashes are therefore frozen explicitly in this note; the
standalone witness-core implementation does not include that dependency.

## 7. Precise remaining boundary

Proved:

1. the frozen source has exactly the four stated holes;
2. every arbitrary nonzero one- or two-position repair of this source fails;
3. all proper-mask witnesses in the waste21 fibre are block-local;
4. the displayed arbitrary-cardinality CNF is exact for that fixed support.

Open until the closure instance is decided:

1. whether arbitrary values on the 21 waste-collar cells complete the source;
2. if not, whether a support using cells outside this collar completes it;
3. the global question whether any other length-12,873 word is universal.
