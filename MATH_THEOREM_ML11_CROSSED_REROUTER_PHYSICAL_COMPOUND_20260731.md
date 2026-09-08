# A physical crossed rerouter exists on `ML(11)`

Date: 2026-07-31  
Status: two explicit Hamilton and matching-floor-tight compounds; exact
dimension-uniform padding lemma; residence failure of the present witnesses;
no guarded all-size recursion yet

## 0. Verdict

The crossed four-by-four service matching is physically realizable.  On the
canonical `ML(11)` MMM Hamilton factor there are explicit replacement
factors which simultaneously:

1. preserve every previously covered lower and upper turn colour;
2. fill exactly the four lower and four upper colours of a crossed q9
   residual rerouter;
3. remain one Hamilton cycle; and
4. raise the augmented occurrence-matching rank from `770` to `774`, exactly
   the new 18-hole integrality floor.

The smallest audited witness found changes 60 middle-level vertices and 30
old factor edges.  Its symmetric difference is the disjoint union

```text
C6 + C16 + C38.
```

Grouped as the two macro bits `C16` and `C6+C38`, all four subset states are
Hamilton and sit exactly at their palette/matching integrality floors.  It
is therefore a genuine coupled rank-tight packet, not a union of the
unavailable independent root `C10` service units.

This closes the **central physical realization** gate left open by the
crossed-Hall theorem.  It does not close the general construction.  The
rank-six projection of the current witness has 151 coordinate runs of
length below four, so it fails the depth-three residence condition.  Its
large common-graph rank drop also shows that floor-tightness is obtained by
a global matching rearrangement rather than four private augmenting paths.
Coexistence with the other q9 packets, deeper providers and the lower
compiler remains to be constructed.

## 1. The fixture and crossed services

Use the canonical labelled MMM gluing selection

```text
(7,8,9,11,12)
```

on `ML(11)`.  Its lower and upper turn defects both have size 22 and its
augmented matching deficiency is 22.  The residual pair is

```text
658,1387.
```

For q9 block 12 the four crossed assignments are

```text
658 -> 1718,
297 -> 1387,
562 -> 827,
1188 -> 1453.
```

Every assignment is a literal containment.  The first and second rows are
the two crossed services; the last two complete the crown matching.

## 2. Explicit physical theorem

### Theorem 2.1 (Hamilton rank-tight crossed compound)

There is a 2-factor `F*` of `ML(11)` with the following properties.

1. `F*` is a Hamilton cycle on all 924 middle-level vertices.
2. Its lower turn support is the source lower support plus exactly
   `297,562,658,1188`.
3. Its upper turn support is the source upper support plus exactly
   `827,1387,1453,1718`.
4. Its augmented occurrence graph has matching size 774 and deficiency 18.
5. Relative to the source factor, it changes the neighbour pair at 60
   vertices, removes 30 old edges and adds 30 new edges.  The symmetric
   difference consists of three vertex-disjoint alternating circuits of
   lengths 6, 16 and 38.

#### Proof

The complete edge list is stored as the witness in

```text
scratch/ml11_crossed_block12_ranktight54_finish_ham_c6c12_20260731.json.
```

The independent audit does not import the CP model.  It reconstructs the
source factor from the defining Dyck/MMM formula, checks every listed edge
is a rank-five/rank-six containment, checks degree two at all 924 vertices,
and traverses one Hamilton component.  It then recomputes every turn
colour.  The final missing sets are literally the source missing sets minus
the four displayed service sets.

Finally it reconstructs the augmented bipartite occurrence graph and runs
an independent augmenting-path matching algorithm.  The result has rank
774.  Since eighteen lower-colour vertices and eighteen upper-colour
vertices are isolated, 774 is the maximum possible rank.  This proves all
five statements. \(\square\)

There is an independent second witness using q9 block 14 and assignments

```text
658 -> 950,
329 -> 1387,
402 -> 475,
804 -> 877.
```

It is also Hamilton and floor-tight; the best retained search witness changes
149 vertices and 79 old edges.  This confirms that the phenomenon is not
tied to one algebraic block choice.

### Theorem 2.2 (two-macro rank-tight cube)

Write the block-12 symmetric difference as `Z6 sqcup Z16 sqcup Z38`, with
the subscript denoting circuit length.  Put

\[
                         P=Z_{16},\qquad Q=Z_6\sqcup Z_{38}.       \tag{2.1}
\]

For every subset of `{P,Q}`, the toggled factor is Hamilton and its
augmented deficiency equals its common lower/upper turn defect.  The four
states have respectively

```text
selected macros     holes/shore     augmented deficiency
none                    22                    22
P                       21                    21
Q                       19                    19
P+Q                     18                    18.
```

#### Proof

The independent audit identifies the three vertex-disjoint alternating
circuits from the literal symmetric difference, toggles all eight circuit
subsets, and recomputes both palettes, physical components and augmented
matching rank.  The four grouped states displayed above are precisely bits
`000,010,101,111`; each has one physical component and equality of defect
and matching deficiency. \(\square\)

## 3. Why the compound is genuinely new

The palette-only optimization has a much smaller exact solution.  It
changes 32 vertices and consists of disjoint alternating circuits

```text
C8 + C12 + C12.
```

That state fills the same four colours on each shore, but has three factor
components and augmented deficiency 20 rather than 18.  Exhausting one
further simple `C6`, `C8`, or `C10` from this state gives no rank-tight
output.  Its best `C10` makes the factor Hamilton and leaves only one extra
matching deficiency.

Thus service Hall, topology and occurrence correlation are three distinct
resources.  The physical witness in Theorem 2.1 crosses the local-circuit
barrier by synchronizing three circuits into the two macro states of
Theorem 2.2.

The common augmented graph of the source and the block-12 witness has rank
739.  The final rank 774 is not an extension of a 770-edge common matching
by four private paths, although the rearrangement is far smaller than in the
first global witness.  Any recursive use must treat `P,Q` as the atomic bits
or carry their full matching interface.

## 4. Dimension-uniform padding

### Proposition 4.1 (padded physical compound)

Let `n>=5`, let the ambient ground have size `2n+1`, and choose disjoint
sets

```text
H, A, G
```

of sizes `n-5,11,n-5`.  Identify `A` with the eleven coordinates of the
base witness.  Replace every base mask `X` by

\[
                            H\cup X.                 \tag{4.1}
\]

Then the source and replacement edge sets of Theorem 2.1 become legal
rank-`n`/rank-`n+1` middle-level factor patches.  Their turn gains are the
four base lower and upper gains padded by `H`; their physical degrees,
symmetric-difference incidence, and augmented containment relations are
unchanged.

#### Proof

Adding the common set `H` raises every rank by `n-5`, preserves containment,
intersection and union, and changes no adjacency.  Coordinates in `G` are
absent from every patch vertex.  Therefore all edge, turn and augmented
incidence equations are identical to the base equations after deleting the
fixed coordinates. \(\square\)

The proposition gives a dimension-uniform **boundaried factor actuator**.
It does not say that an arbitrary host factor contains its old boundary, or
that the host's external path pairing makes the replacement topology-safe.
Those are installation guards.

## 5. Exact guard ledger

For the block-12 witness the signed turn banks are

```text
lower: 16 negative units, 16 positive units, 32 changed colours;
upper: 16 negative units, 16 positive units, 32 changed colours.
```

No colour loses more than one occurrence, and no support member is lost.
Consequently a host with one declared spare occurrence for every negative
colour passes the central provider guard.  This is finite data independent
of `n` after padding.

The other rows do not follow from central support.

* **Residence.**  In the rank-six projection of the present Hamilton cycle,
  156 coordinate runs have length two or three.  Hence this witness is not
  a depth-three carrier.
* **Deeper providers.**  Reordering a Hamilton cycle can alter windows far
  from an individual changed seam.  One must reserve the complete developed
  component or export the exact negative-part table; edge support alone is
  insufficient.
* **Compiler Hall.**  The final central matching does not imply a common
  lower-cell SDR.  The old/new compiler banks require the exact common-cap
  inequality from the translated-packet theorem.
* **Packet coexistence.**  Six untouched q9 defect blocks remain.  The
  present theorem does not install their physical packets disjointly from
  the crossed compound.

An atomic guarded installation is valid under the already-proved general
conditions: a private boundaried old patch, topology-compatible external
ports, the complete negative-part provider reserve, an accepting residence
boundary transformation, and a common compiler-Hall bank.  Proposition 4.1
makes all local tables finite, but existence of those reserves in the MMM
recursion is the remaining theorem.

## 6. The sharpened general target

The service basis and central physical basis are now both finite.  The
remaining regenerative statement can be isolated as follows.

> **Guarded two-packet regeneration.**  Choose the MMM gluing state so that
> its turn debt decomposes into q9 blocks plus crossed residuals; install
> pairwise compatible padded q9 packets and padded crossed compounds; and
> choose their common decoration so that residence, all protected providers,
> physical forest topology and lower compiler Hall survive.

Theorem 2.1 proves that the crossed compound exists before those common
guards are imposed.  A positive joint residence solve on the same base, or
a transparent compound carrying a common decoration, would close the next
substantial layer.  A failure would not refute the formula; it would show
that this particular stateless MMM regeneration needs a larger carried
state.

## 7. Reproducibility and scope

Run

```text
python3 scratch/audit_ml11_crossed_rerouter_physical_packet_20260731.py
```

to produce

```text
scratch/ml11_crossed_rerouter_physical_packet_20260731.audit.json.
```

The finite theorem quantifies only over the two displayed edge-list
certificates.  The palette-only minimum and the short finishing-circuit
census are separate solver/audit scopes and are not used to prove existence
in Theorem 2.1.  No minimum-support, all-factor, all-dimension guarded, or
`nu=B` conclusion is asserted here.
