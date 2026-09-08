# K17 shared lower-turn shell and exact elementary service law

Date: 2026-07-31  
Status: exact solver-free audit of the six frozen K17 old-rail banks; exact
elementary service theorem; no factor switch, decoration, or full ordered
four-transversal claim

## 1. Scope and verdict

The six banks

```text
source, hard361, hard323, quick650, soft437, active2649
```

are reconstructed from the same independently hashed eleven-cycle PBBS
rank-nine factor.  A lower turn at a defined centre `v` is

\[
       \ell(v)=\operatorname{pred}(v)\cap v\cap\operatorname{succ}(v)
       \in\binom{[17]}7.
\]

Their missing lower-turn sets have exact intersection

\[
                         |\mathcal C|=1297.             \tag{1.1}
\]

This is the literal minimum persistent support core shared by all six
banks.  It is not a complete augmented-trace Hall witness and it is not a
four-transversal defect: only the represented old rail is present.

Every member of `C` nevertheless has an elementary upper-surjection-safe
one-arc realization in every bank.  Thus the shared support deficit is not
caused by the absence of local Johnson providers.  The remaining obstruction
is correlating those providers into a degree-balanced physical switch packet
whose collateral lower turns and common-core augmenting linkage pass.

## 2. Exact shared deficit ledger

The six missing-set sizes are

\[
3826,\ 4411,\ 4442,\ 4611,\ 4442,\ 4929.
\]

Their union has size `9002`.  The number of targets missing in exactly
`j` of the six banks is

\[
 1^{3303}\,2^{1342}\,3^{774}\,4^{860}\,5^{1426}\,6^{1297}. \tag{2.1}
\]

Among the `3826` source holes, the number surviving in exactly `j` of the
five successor banks is

\[
 0^{11}\,1^{64}\,2^{295}\,3^{746}\,4^{1413}\,5^{1297}.     \tag{2.2}
\]

Conversely, among targets supported by the source but lost by at least one
successor, the number lost by exactly `j` successors is

\[
 1^{3292}\,2^{1278}\,3^{479}\,4^{114}\,5^{13}.             \tag{2.3}
\]

Equations (2.2)--(2.3) show why total lower-hole count is not a switch
potential: every bank repairs many source holes while simultaneously
creating a different shell.

The induced Johnson-distance-one graph on `C` has `3486` edges and component
orders

\[
                         1285,3,1^9.                 \tag{2.4}
\]

After adding pairs at Johnson distance two it is connected, with `47170`
edges.  Thus the persistent core is not separated into many invariant local
classes at the two-coordinate scale.  This connectivity is only a candidate
generation fact; it does not itself produce a physical alternating circuit.

There is nevertheless a sharp one-coordinate shell profile.  For a rank-six
core `R`, count extensions `R+x` in `C`; the maximum is five, attained by
exactly nine cores

```text
08469 08994 089c4 10b50 11223 11c09 120ca 12930 148a4.
```

For a rank-eight cap `K`, count deletions `K-x` in `C`; the maximum is also
five, attained by exactly

```text
0c9d4 1187a.
```

The complete multiplicity histograms are

\[
\begin{array}{c|rrrrr}
\text{multiplicity}&1&2&3&4&5\\ \hline
\text{rank-six extension shells}&4130&1680&400&86&9\\
\text{rank-eight deletion caps}&7456&2110&380&36&2.
\end{array}                                          \tag{2.5}
\]

These are exact catalogue maxima, not a theorem that one physical switch
can realize all five entries of a shell.

## 3. The exact service-shell theorem

Let `F` be any directed two-factor on the rank-nine subsets of `[17]` such
that its edge intersections biject the rank-eight subsets.  For an incident
edge at a centre `v`, call the unique coordinate in `v` but not in the other
endpoint its **deletion label**.

### Theorem 3.1 (twenty-half-port law)

If `L` is a missing rank-seven lower turn of `F`, then:

1. exactly twenty distinct centre/incident-edge pairs have deletion label
   in `v-L`;
2. at each such half-port, retaining that incident edge and replacing the
   opposite factor edge can create turn `L`;
3. there are exactly eight choices for the new opposite neighbour; hence
   there are exactly `20*8=160` raw elementary service records.

#### Proof

There are ten rank-eight supersets `X=L+x`.  Lower-rainbowness gives one
factor edge `e_X` with intersection `X`.  Its two rank-nine endpoints give
two half-ports whose deletion labels are the respective coordinates outside
`X`.  This gives twenty incidences.

No two of them can have the same centre.  If the `X`-edge and `Y`-edge met
at one centre, they would be its two factor edges and their intersection
would be (X\cap Y=L), so `L` would already occur as the lower turn there.

At a half-port with centre `v=L+a+b`, retain the incident edge deleting
`a`.  Replace the opposite edge by the edge from `v` which deletes `b` and
adds `c`.  There are exactly eight choices `c notin v`, and the resulting
two deletion labels are `a,b`; hence the new turn is `L`.  The incoming
version is identical.  This proves all three assertions.  `square`

### Lemma 3.2 (exact isolated upper-palette count)

Suppose the opposite edge removed at a service half-port has rank-ten union
colour `U=v+c_0`.

* If `U` has another occurrence, all eight replacements preserve upper
  surjectivity.
* If `U` is unique, exactly one replacement preserves upper surjectivity:
  use the same added coordinate `c_0`.  The new edge then has union `U`
  literally.
* At a path endpoint where no opposite edge is removed, all eight choices
  are upper-safe.

Consequently, if a bank has `h` raw service half-ports and `d` of their
opposite arcs are absent or have repeated upper colour, the exact number of
isolated upper-surjection-safe service records is

\[
                              h+7d.                  \tag{3.1}
\]

#### Proof

Every replacement union is `v+c`.  It equals the lost union `v+c_0` iff
`c=c_0`.  If the lost colour has another occurrence there is no constraint
on `c`; otherwise equality is necessary and sufficient.  No colour is lost
at an empty endpoint.  `square`

The same-union option is essential.  Counting only opposite arcs whose old
upper colour is repeated would incorrectly report zero providers for three
bank/target pairs.

## 4. Exact finite shell census

On the common set `C`, the source has exactly twenty half-ports for every
target, as Theorem 3.1 requires.  The five partial path/cycle banks need not
be lower-rainbow or two-regular after cuts, and their half-port counts vary:

| bank | raw half-port range | minimum upper-safe records | minimizers |
|---|---:|---:|---|
| source | 20 | 27 | 55393, 75278, 75896, 85130, 88176, 92210 |
| hard361 | 12--24 | 16 | 92210 |
| hard323 | 12--24 | 16 | 83718 |
| quick650 | 12--26 | 16 | 82800 |
| soft437 | 10--26 | 21 | 59480, 68820 |
| active2649 | 10--26 | 21 | 36124, 55372 |

In particular, none of the `6*1297` bank/target pairs lacks an isolated
upper-safe elementary service record.  For targets 92210, 83718, and 82800
in the displayed respective banks, all sixteen safe records are the
same-union choices from sixteen unique-colour opposite arcs.  They are the
sharpest elementary shells, not no-provider obstructions.

The twenty source half-ports of a common target lie in between one and seven
of the eleven source cycles.  The exact target histogram by number of source
cycles met is

\[
             1^{65}\,2^{17}\,3^{184}\,4^{570}\,
             5^{371}\,6^{85}\,7^5.                 \tag{4.1}
\]

Thus sixty-five persistent targets already have their entire raw service
shell inside one source component.  This makes internal compound switches
plausible for those rows, but it does not guarantee factor topology or a
common-core matching repair.

## 5. The source has an additional correlation deficit 308

The complete source, unlike the five partial banks, supports the full
componentwise augmented trace graph.  Its two shores each have size `43758`,
it has `97240` edges, and an independently replayed maximum matching has
size

\[
                             39624.
\]

Hence its exact augmented deficiency is

\[
               43758-39624=4134=3826+308.           \tag{5.1}
\]

The first term is forced by the `3826` isolated missing rank-seven colour
vertices.  The second is genuine incidence correlation.  An explicit
alternating-closure Hall row remains after the isolated vertices are
deleted:

\[
\begin{array}{c|rr|r}
 &\text{rank-eight positions}&\text{supported rank-seven colours}
 &|X|\\ \hline
 X&823&1261&2084
\end{array}
\]

and its neighbourhood has

\[
\begin{array}{c|rr|r}
 &\text{rank-nine positions}&\text{rank-ten colours}&|N(X)|\\ \hline
 N(X)&1380&396&1776.
\end{array}
\]

Thus `|X|-|N(X)|=308` literally.  Reversing every canonical vertex and
adjacency order produces a different maximum matching but the same four
literal Hall sets.  By contrast, the *types of the exposed vertices of one
maximum matching are not invariant*: one maximum matching can expose right
rank-ten vertices while another exposes right rank-nine vertices.  Only the
literal Hall row or a fixed common-core matching may be used as a linkage
The literal Hall sets, rather than any exposed-type histogram, form the
reusable common-core linkage signature.

There is an immediate scale obstruction.  A Hamilton-safe alternating
`2t`-circuit contributes at most `3t` genuinely new augmented edges.  If a
packet repairs `s` old missing colours and is **shell-tight**, meaning its
new deficiency is at most the remaining isolated floor `3826-s`, then its
matching rank must rise by at least `308+s`.  Therefore

\[
                         t\ge \left\lceil{308+s\over3}\right\rceil.
                                                               \tag{5.2}
\]

Already for `s=1`, shell-tight repair requires `t>=103`.  This does not
forbid a shorter packet from increasing lower-turn support while leaving a
positive correlation excess; it proves that no bounded small polygon can
simultaneously install even one source hole and reach the new missing-colour
floor.

## 6. Proof-safe packet prefilter

For a proposed compound packet with deleted arc set `D` and added arc set
`A`, the following order is exact and inexpensive.

1. Enforce directed indegree/outdegree balance and literal arc distinctness.
2. For every rank-ten colour `U`, enforce

   \[
       c_U-|D\cap E_U|+|A\cap E_U| \ge 1.            \tag{6.1}
   \]

   Same-union elementary records satisfy their local row identically.
3. Replay every changed lower turn, including the neighbouring centres, and
   score actual support gain rather than intended service labels.
4. Form the common augmented graph `H=G\cap G'`.  For a declared target
   deficiency `q`, accept the packet only if its genuinely new augmented
   edges satisfy the item2167 rows

   \[
       |N_A(X)\setminus N_H(X)| \ge |X|-|N_H(X)|-q
       \quad\hbox{for every left set }X.             \tag{6.2}
   \]

   Equivalently, require enough vertex-disjoint exposed-terminal augmenting
   paths to reduce the common-core deficiency to at most `q`.  Taking `q=0`
   is the complete occurrence-flow gate; taking `q=4134-s` is the exact
   excess-nonincreasing test after installing `s` source holes.

Steps 1--3 are candidate-generation filters.  They do not replace (5.2): a
packet can preserve both marginal turn surjections and still create a new
component-Hall witness.

## 7. Reproduction and scope

Run

```text
python3 scratch/threadD_audit_k17_shared_lower_turn_shell_20260731.py
```

It authenticates the six prior diagnostic payloads and their candidates,
reconstructs every missing set and service half-port, verifies the
twenty-half-port law on all 1297 common targets, and writes the full common
target list plus the minimum service records to

```text
scratch/threadD_k17_shared_lower_turn_shell_20260731.audit.json
```

The independently ordered augmented-rank and active-Hall replay is

```text
scratch/threadD_audit_k17_source_active_hall_witness_independent_20260731.py
scratch/threadD_k17_source_active_hall_witness_independent_20260731.audit.json
```

The separate primary shell/rank audit and literal common-mask list are

```text
scratch/threadD_audit_k17_lower_turn_shell_20260731.py
scratch/threadD_k17_lower_turn_shell_20260731.audit.json
scratch/threadD_k17_lower_turn_shell_20260731.masks.txt
```

The audit is deliberately old-rail and local.  A passing elementary record
is not a directed factor switch; no middle-levels decoration test applies to
the partial banks; and no partial atom ledger is promoted to a full ordered
four-transversal.
