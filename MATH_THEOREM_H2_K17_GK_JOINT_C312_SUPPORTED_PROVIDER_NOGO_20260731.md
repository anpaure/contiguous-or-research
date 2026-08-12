# The joint `c=312` cut/bundle certificate fails the supported-provider Hall gate

Date: 2026-07-31  
Status: independently replayed, fixed-certificate **NO-GO**.  This is a
source-relative statement about one `312`-edge cut set and one displayed
first-bundle choice, not an unrestricted `k=17` no-go.

## 1. Literal certificate

The frozen joint certificate

```text
scratch/k17_gk_joint_cut_bundle_ad6fb0631c9c336f_20260731.json
SHA-256 ad6fb0631c9c336f229846cdb2a78a8f1a8f3a6532968310b964f5f560c0e9e4
```

contains `312` pairwise vertex-disjoint cuts.  Exact replay gives `90`
endpoint--internal and `222` internal--internal cuts, on `624` distinct old
vertices.  The residual forest has

\[
 9840\text{ edges},\quad 5536\text{ components},\quad
 10892\text{ terminals},\quad90\text{ isolated old vertices},\quad
 4394\text{ retained turns}.                                  \tag{1.1}
\]

Thus it has `2536` missing rank-six colours, `14470` fresh rank-eight
colours and `19916` fresh rank-nine colours.

The certificate also fixes `380` first edges.  Their exposure-cut loads are
`1^244 2^68`; their rank-six colours, old ports, unused partners, rank-eight
unions and boundary rank-nine turns are each separately distinct.  Dynamic
owner replay gives

| resource | natively fresh | released by exposure cut | released by another cut |
|---|---:|---:|---:|
| rank 8 | 106 | 268 | 6 |
| rank 9 | 107 | 268 | 5 |

Every non-native rank-nine turn is destroyed by exactly one selected cut.
The recorded CP-SAT optimality values are not reproved here; only the literal
certificate is needed below.

## 2. Conservative cut-relative supported relation

Let `T` be the residual degree-one old vertices, `Z` the `90` isolated old
vertices, and `U` the `4072` old-unused rank-seven vertices.  Candidate new
edges live on `T union Z union U`.  They avoid only the retained rank-eight
palette.  At `T` their retained-neighbour boundary turn must avoid the
retained rank-nine palette.  At `U` every selected edge must belong to a
surviving fresh centred wedge.

For proof safety, the support peel is deliberately relaxed at `Z`: an edge is
not deleted merely because it lacks an isolated-centre wedge.  This allows
all `90` isolated old vertices to behave as possible final endpoints, whereas
a real path can use at most two.  The relation is therefore an enlargement of
every legal completion face.

As usual, join a missing rank-six colour `c` to a fresh rank-eight colour `q`
when the greatest supported edge set contains a carrier with intersection
`c` and union `q`.

### Theorem 2.1

Any locally clean arbitrary-length, rank-eight-rainbow ear completion on this
fixed cut set induces a matching saturating all `2536` left rows of the
cut-relative supported-provider graph.

### Proof

Every chosen carrier edge and every chosen wedge at an inserted unused vertex
form a post-fixed subsystem of the monotone support operator.  Consequently
all chosen carriers survive the greatest peel.  Choose one carrier for each
missing rank-six colour.  Their rank-eight unions are pairwise distinct in a
rank-eight-rainbow completion, and hence form the claimed matching.  Relaxing
the isolated vertices can only add supported carriers. \(\square\)

## 3. Exact Hall obstruction

On the exact joint-certificate cut set, the conservative catalogue has

\[
\begin{array}{c|rr}
&\text{raw}&\text{after support peel}\\\hline
\text{edges}&162360&160396\\
\text{wedges}&4589382&4549771.
\end{array}
\]

The resulting provider relation has

\[
\begin{array}{c|c}
\text{left rows}&2536\\
\text{right rank-eight resources}&7483\\
\text{incidences}&43711\\
\text{zero rows}&1\quad(c=476)\\
\text{matching rank}&2447\\
\text{deficiency}&89.
\end{array}                                                     \tag{3.1}
\]

The canonical alternating-reachable Hall shore has `265` rank-six rows and
exact neighbourhood of size `176`:

\[
                             265>176.             \tag{3.2}
\]

Theorem 2.1 and (3.2) prove that this fixed cut set has no supported
rank-eight-rainbow ear completion.  This computation does **not** condition
on the `380` fixed bundles; it is a relaxation which permits every locally
supported carrier in the dynamic palettes.  Therefore charging the fixed
bundles cannot repair the deficiency.  In particular, not all `2536` rows can
be matched after those bundles.

There is also a still earlier obstruction specific to the displayed bundle
choice.  Once each fixed port--partner edge consumes its rank-eight and
boundary rank-nine resources, its unused partner needs one compatible
continuation edge.  Exact local replay finds `75` partners with no such edge
(the first is colour `1621`, partner `1877`).  Even granting two of them as
global endpoints leaves `73`.  This corroborates but is not needed for the
stronger unconditioned Hall no-go.

## 4. Authenticated replay

Cut/bundle and conditioned-continuation audit:

```text
scratch/audit_h2_k17_gk_joint_first_bundle_20260731.py
SHA-256 bd78665ba3067895d565476a3fd9415f10bc3fad6e336a22e3973a914a6a160d

scratch/h2_k17_gk_joint_first_bundle_20260731.audit.json
SHA-256 17b48f37ece2e881f1d5f8601a58e9d98e32ae69509d1298081af1930f4739a2
canonical payload 24632ac9e7f110fd42af021c238c728ebfe9064122af8406196f5b62b559a0df
```

Supported-provider generator and output:

```text
scratch/h2_scan_k17_gk_joint_cut_supported_provider_20260731.cpp
SHA-256 7f2d63d771b773d0ecb1424d39e9e8f1f3e62f9c72968a13019d4056925ef5dc

scratch/h2_k17_gk_joint_ad6fb_supported_provider_20260731.audit.json
SHA-256 293b588f37df4e77ce56dab56532ec520edee863e04e000dd41aa8227508f169
```

Independent explicit-relation, matching and DM verifier:

```text
scratch/verify_h2_k17_gk_joint_ad6fb_supported_provider_20260731.py
SHA-256 aaee2d57d99038878571212949878aced3f2031ad8e4a86a1d158559330e00db

scratch/h2_k17_gk_joint_ad6fb_supported_provider_20260731.verify.json
SHA-256 813f42d11579d322a821648e093fbb827cd771c1b99e4e9f718133608b2b2dee
canonical payload dff23867a5e49b0faa86bf1f8dffae7b1feaac9b0fdb4ebb88348cc7ef34a112
```

The verifier reconstructs the dynamic retained palettes from the exact cut
IDs, validates every emitted `(rank6,rank8)` incidence, recomputes both
codegree tables and a separate Hopcroft--Karp matching, and verifies that the
displayed `176` masks are exactly the neighbourhood of the displayed `265`
masks.  The scope excludes other cut sets, joint reoptimization of cuts and
bundles, the prefix, higher shadows, residence, common cap and any `k=17`
word claim.
