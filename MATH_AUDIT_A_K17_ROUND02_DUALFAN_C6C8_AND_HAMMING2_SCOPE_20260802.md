# Counteraudit of the round02 dual-fan circuit census and exact final-net pruning

Date: 2026-08-02  
Lane: A, independent physical-socket/circuit audit  
Status: **C6 and star-C8 no-go verified; unrestricted C8 and Hamming-two no-go not proved**

This note supersedes the broader scope wording previously attached to the
round02 `114930` dual-fan census.  There are two substantive corrections.

1. The C8 generator is exhaustive only for the rank-seven-core **star**
   family.  It does not generate the rank-six-core **octahedral** family.
2. Several census columns use rebuilt numeric path identifiers as though
   they were stable physical roles.  They form a conservative candidate
   filter, not an exact census of role relocations or two-arm socket escapes.

The corrections do not invalidate the exact negative result for the move
classes actually enumerated.  They do change its theorem boundary.

## 1. Frozen instance and exact conclusion

The frozen inputs have SHA-256

```text
factor                 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
round02 bank           48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649
protected C6 catalogue f2c948de733a5286f4d21c3ba3cd2507831e2b061ca59f7fe82ace5c11b55d67
```

The physical socket owners are

\[
        s=115442,\qquad t=115186,
\]

and the incumbent fixed-bank obstruction is their one-colour dual fan at
lower colour `114930`.

The exact finite theorem supported by the artifacts is the following.

> **Theorem 1.1 (scoped circuit no-go).**  In the frozen round02 bank:
>
> 1. no member of the authenticated 46,818-row protected simple C6
>    catalogue yields a locally admissible exact-q1/rank-ten completion;
> 2. no protected simple C8 of star form
>    \(C_i=S\cup\{a_i\}\), with \(|S|=7\), yields such a completion;
> 3. no conclusion follows for octahedral C8s
>    \(C_i=S\cup\{a_i,a_{i+1}\}\), with \(|S|=6\), or for compound
>    circuits, recut-plus-circuit moves, or adaptive cut banks.

The exact 65 compatible unordered pairs drawn from the twelve certified
visible one-recut socket escapes are also exact-q1 UNSAT.  This is a
final-net statement for that 12-row menu; it is not a full Hamming-two
no-go.

## 2. Owner-stable support criterion

The correct local object is occurrence-labelled and is independent of
mutable path numbers.

Fix a selected lower-colour bank \(D\), rebuild the physical path forest,
and anchor the two roles by the owner masks \(s,t\).  For a socket owner
\(x\in\{s,t\}\), let \({\cal A}_D(x)\) be the set of admissible directed
arms

\[
       (x,\epsilon)\longrightarrow(y,\eta)
       \quad\hbox{labelled by}\quad (c,u),
\]

where the endpoint states are identified by their ordered owner sequence
and orientation, \(c\in D\) is the selected lower colour, \(u\) is the
upper union, and the Johnson, residence, and resource predicates all hold.
The outside endpoint is the physical owner occurrence \(y\), not the
integer index of its rebuilt path.

Let \(G_D(s,t)\) be the bipartite resource graph with left side
\(\{s,t\}\).  An arm is adjacent to the resource consisting of its lower
colour, outside endpoint occurrence, and any orientation/capacity resource
used by the exact formula.  A direct admissible \(s\)-to-\(t\) seam is
represented as a two-socket resource.

> **Lemma 2.1 (exact fixed-role escape test).**  If the forced socket roles
> remain at the same owner occurrences, the frozen two-socket certificate
> is destroyed exactly when either
>
> * an admissible direct \(s\)-to-\(t\) seam exists; or
> * the two sockets have a resource-disjoint pair of arms, equivalently
>   \(\nu(G_D(s,t))=2\).
>
> In the reduced dual-fan table this is the familiar condition of distinct
> lower colours and distinct outside socket occurrences.

This is merely the local certificate test, not global q1 feasibility.  If a
move changes a forced role, one must locate the new role by owner/occurrence
data and rebuild the table there.  Touching the old numeric component is not
itself a role relocation.

The test depends on the full support symmetric difference.  A move that
deletes and adds the same number of atoms can still replace the only arm at
a socket.  Degree preservation, the multiplicity of colour `114930`, or a
zero net count is therefore not a safe pruning rule.

## 3. Exact dependency cone

For a socket owner \(x\), define

\[
 N_D(x)=\{y: |x\cap y|=8,\ x\cap y\in D\}.
\]

Let \(P(z)\) be the incumbent path containing owner occurrence \(z\), and
put

\[
 {cal K}_D(s,t)=\{P(s),P(t)\}\cup
     \{P(y):y\in N_D(s)\cup N_D(t)\}.
\]

For a circuit \(\Gamma\), let \({\cal S}(\Gamma)\) contain every old path
component incident with a deleted or added incidence of \(\Gamma\).  This
definition includes count-neutral changes.

> **Lemma 3.1 (sound cone pruning).**  If
> \({\cal S}(\Gamma)\cap{cal K}_D(s,t)=\varnothing\), then the socket
> roles and every possible selected-colour arm incident with them are
> unchanged.  Hence the frozen dual-fan certificate persists.

**Proof.**  The two socket paths are outside the changed support, so their
endpoint occurrences and orientations are fixed.  Any selected-colour arm
incident with a socket \(x\) has other owner \(y\in N_D(x)\), whose old
path lies in \({\cal K}_D(s,t)\).  Such an arm cannot be added or deleted
by a circuit disjoint from the cone.  Thus the occurrence-labelled local
table is identical.  \(\square\)

This cone is a no-false-negative prefilter.  Meeting it is neither
sufficient for escape nor a proof that a displayed numeric state is a true
socket state.

## 4. The missing C8 family

The complete simple incidence-C8 classification has two disjoint forms.

* **Star:** \(C_i=S\cup\{a_i\}\), \(|S|=7\).  Opposite lower vertices
  have Johnson distance one.
* **Octahedral:**
  \(C_i=S\cup\{a_i,a_{i+1}\}\), \(|S|=6\), indices modulo four.
  Opposite lower vertices have Johnson distance two.

This classification is proved in
`MATH_AUDIT_R_K17_PROTECTED_C8_CLASSIFICATION_CUT_AND_DUPLEX_20260731.md`.

The audited generator in
`scratch/threadD_k17_round02_dualfan_c6c8_20260801.cpp` loops only over
rank-seven cores and calls

\[
       C_i=S\cup\{a_i\}.
\]

It therefore enumerates every orientation of the star family:

\[
 \binom{17}{7}\binom{10}{4}\,3\,2=24,504,480
\]

keys, where the last factors are the three cyclic orders of a four-set and
the two toggle phases.  It enumerates no octahedral C8.  The omitted family
has independently the same number of canonical oriented keys,

\[
 \binom{17}{6}\binom{11}{4}\,3\,2=24,504,480.
\]

Thus “complete C8” in the census source/audit scope string must be read as
“complete star-C8.”  A complete simple-C8 master must add the rank-six-core
octahedral loop and apply the same protected-incidence, cone, final-net,
and exact-formula checks.

## 5. What the 138-row census columns do and do not certify

The census source has SHA-256

```text
1f0e3a9aa9e4389aa4ad689bd67c78b0c10e96066511000773abf0f5b9fd3e5a
```

and its reproduced table/audit have SHA-256

```text
census 85a092ce915623ff0dc7e1ee789f3fab7d1f72b52980bf42c300f7e4ba9ce59b
audit  3645537503ccd4319dcf95a9887dc5d27896de0819525595945fae243b3f79dc
```

The exact declared-catalogue counts are

| object | count |
|---|---:|
| protected C6 catalogue | 46,818 |
| C6 meeting the dependency cone | 373 |
| oriented star-C8 keys | 24,504,480 |
| active protected star-C8 keys | 54,463 |
| star-C8 meeting the cone | 500 |
| conservative candidate rows | 138 |
| rows passing all local gates | 2 |
| local-gate C6 / star-C8 | 2 / 0 |

The labels `role_rethread`, `noncore_socket_adds`, and
`central_st_adds` are not owner-stable physical classifications.

* `role_rethread` is set exactly when an **old numeric socket piece id** is
  among the affected old pieces.  It means “central old component touched,”
  not “the forced owner role moved.”
* Rebuilt paths are lexicographically sorted and renumbered.  Added atoms
  are then compared with baseline numeric state ids.  Consequently an atom
  printed at rebuilt state `3670` need not be incident with owner `115442`.
* The candidate predicate accepts any such apparent noncore addition; it
  does not demand a matching arm at the opposite socket, distinct colours,
  or distinct outside resources.

For example, C6 `26029` changes no incidence at physical owners `115442`
or `115186`.  Its 34 recorded “socket additions” are attached to a rebuilt
state numbered `3670` whose endpoint owner is `115324`.  Hence neither the
number 34 nor the flag `role_rethread=1` is an exact physical escape
statement.

The 138 rows are therefore a conservative candidate superset, not an exact
count of role relocations, direct seams, or two-arm escapes.  This is enough
for the scoped negative: only C6 `26029` and `44796` pass all additional
local gates, and the exact q1/rank-ten formulas stored for both are UNSAT.
No star-C8 reaches that downstream gate.

The stored DRAT proofs have SHA-256

```text
26029 22341b0a64e7095d62fb11d60680dca6b1e868b3d8b19536663288c32307512c
44796 a3b88a3fa970d13a246a9a6c412fc444b9bd04fbe265f2aa1836a2735d53ee83
```

and both stored full checks and compact-core checks report `s VERIFIED`.
Their common compact contradiction lies on untouched pieces
`243,244,3262`, lower colours `74383,67215`, and orientation variables
`487,488,489,490`.  It is a second frozen q1 core, showing why escaping the
priced `114930` table need not make the global formula feasible.

There is one lineage caveat.  The archived proofs authenticate the archived
CNFs.  The priority audit records replay-source SHA
`dc206294dd92181637ea2809c2feb06d4219fffdbc85c32a567e451c8eae208c`,
whereas the currently copied builder source has SHA
`407ce6fb36624fffd05061966248dc8155dcaf26864ed319bfab0b9ae2be27e9`.
No byte-identical source-to-CNF regeneration under the former source is
present locally.  The finite formula UNSAT is authenticated; completely
reproducible semantic builder lineage requires preserving or restoring the
exact frozen builder.

## 6. Compound moves must be tested at their final net state

Let \(g_1,\ldots,g_k\) be compatible local changes.  Their relevant object
is the final incidence/cut assignment after all cancellations, not the list
of individually accepted prefixes.

> **Lemma 6.1 (final-net rule).**  An exact compound-circuit enumerator must
> apply the complete net move, rebuild paths and occurrence-labelled roles
> once, and then evaluate all local and global resources.  It is unsound to
> require every proper prefix to be feasible, and it is unsound to sum only
> scalar degrees.

Indeed, two individually visible arms can compete for the same outside
resource and fail jointly.  Conversely one change can expose a raw endpoint
adjacency while another selects its colour or repays its local debt; neither
prefix need be a certified escape.  These are precisely the two directions
lost by prefix filtering.

For a family of frozen small UNSAT tables \({\cal T}_1,\ldots,{cal T}_r\),
a proof-safe pruning rule is:

\[
  \text{retain }\Gamma\text{ only if, for every }j,
  \text{ the final net move changes a role/resource clause of }{cal T}_j
  \text{ or the rebuilt local table }{cal T}_j(\Gamma)\text{ is feasible}.
\]

If one occurrence-labelled table is literally unchanged, its contradiction
persists.  This criterion includes count-neutral changes and is stronger
than pricing only the `114930` degree.

## 7. Exact Hamming-two trichotomy and the conditional 21-anchor master

Let \(g,h\) be distinct-base one-for-one recuts, let \(C_g,C_h,C_{gh}\)
be their two one-change children and joint child, and let \(K(C)\) be the
selected lower-colour set of a child.  Suppose neither recut changes a
central base.  Anchor socket roles by owner occurrence.

For a recut \(g\), let \({\cal R}_g\) be its **raw** new central-to-leaf
seams satisfying endpoint and residence predicates, before asking whether
their colours are selected.  Write \(\gamma(e)\) for the lower colour of a
raw seam.

> **Theorem 7.1 (exact joint-activation trichotomy).**  Assume the standard
> recut locality rule: a recut changes endpoint geometry only in its own base
> piece, while membership of a raw seam in the selected atlas factors into
> its endpoint/residence predicate and selection of its lower colour.  If the
> joint child \(C_{gh}\) destroys the frozen dual fan, then at least one of
> the following occurs:
>
> 1. the joint child relocates a forced socket role, in which case the old
>    fixed-role table no longer applies and the new role must be rebuilt;
> 2. `g` or `h` is one of the nine central recuts in bases `1834,1835`;
> 3. one single child already has an admissible socket escape;
> 4. with the roles fixed, there is a joint-only cross activation, namely an
>    \(e\in{cal R}_g\) with
>    \(\gamma(e)\notin K(C_g)\) but
>    \(\gamma(e)\in K(C_{gh})\setminus K(C_g)\), or the symmetric condition
>    with `g,h` exchanged.

**Proof.**  Remove the role-relocation and central-base cases.  The central endpoint states and
the direct \(s\)-to-\(t\) predicate are fixed.  Any new breaker therefore
uses a central-to-leaf seam.  Its changed leaf endpoint belongs to one of
the two recut bases, so its raw endpoint/residence predicate already occurs
in that one-change child.  If its colour is selected there, that child is
an individual escape.  Otherwise the seam exists only because the other
recut changes the selected-colour bank, giving case 3.  \(\square\)

The direct \(s\)-to-\(t\) seam cannot be activated by two noncentral
recuts, since both central endpoint states and its selected colour remain
fixed.

This theorem gives the exact condition missing from the proposed
`12 visible + 9 central` reduction.  That 21-anchor master is complete only
under all three extra hypotheses:

1. the two forced socket roles remain fixed;
2. each one-change child is required to satisfy the individually frozen
   zero-265 rows; and
3. the raw-atlas/colour-delta test above proves that no joint-only cross
   activation occurs.

Without these hypotheses it is not complete.  A dirty one-change child can
have its debt cancelled by the partner, and a cross-activated seam may be
absent from both individually selected-colour atlases.

The central scope must also remain unpruned.  Only
`1834:9924->9923` is individually zero265-clean.  The recut
`1835:9933->9932` and the other seven central recuts fail at least one local
row individually, but a second recut can cancel that debt.  All nine belong
in the final-net Hamming-two master.

The smallest proof-safe noncentral master records, for every recut `g`,

* its raw seam atlas \({\cal R}_g\);
* the added and removed selected-colour sets;
* its occurrence-labelled resource and local-debt deltas; and
* whether it changes a central role.

A pair is retained if it is central, individually escaping, cross-activating
by Theorem 7.1, or capable of cancelling a local/table debt.  The pair is
then rebuilt and checked only at the final state.

## 8. The exact 12-row pair no-go

There are \(\binom{12}{2}=66\) unordered pairs of certified visible clean
one-recut escapes.  One same-base pair is incompatible.  The remaining 65
were composed at final net state; all preserve the scoped zero265 rows and
all exact q1 formulas are DRAT-verified UNSAT.

The frozen hashes are

```text
pair audit       fe5fb127e9d405574f9e1b7da7f2cc7fcdb98794ce0a881e6497819099123b70
pair table       7b2edd1557f4fe94e6c88acdc362ffb18b88cd21f8bf6e03eb3699f5c89556b7
q1 summary       b2cdcece539162e9a0eee4ad4ebcdfc0597cc075e0b8732674511753add8a39b
DRAT summary     006c2c09177248228cf40a20d78472ee28abcc581c95308050546f3db6a1f3f3
```

This proves that individually visible arms do not acquire a useful
synergy merely by pairing.  It says nothing about a pair involving a dirty
recut, any of the nine central recuts, or a joint-only cross activation.

## 9. Acceptance checklist for the next exact layer

An exact C6/C8 or Hamming-two claim is accepted only if all of the following
are explicit.

1. **Universe and hashes.**  Freeze the factor, cut bank, move generator,
   formula builder, solver/checker, and output hashes.
2. **Complete move class.**  State whether C8 means star, octahedral, or
   both.  For “all simple C8,” enumerate both 24,504,480-key families.
3. **Final-net construction.**  Apply all changes and cancellations before
   testing; do not impose prefix feasibility unless chronology explicitly
   requires it.
4. **Owner-stable roles.**  Locate `115442,115186` and every forced role by
   owner occurrence/path fingerprint after rebuilding.  Never infer role
   relocation from a reused numeric path id.
5. **Full support delta.**  Compare occurrence-labelled incidence support,
   not degrees.  Retain count-neutral replacements.
6. **Exact local escape.**  Rebuild the direct seam and both arm atlases and
   compute the resource matching rank \(\nu(G_D(s,t))\), including distinct
   colours, outside occurrences, orientations, and capacities.
7. **Cross activation.**  For compound recuts, build raw endpoint atlases
   before colour filtering and test them against the other move's colour
   delta.
8. **Dirty-pair cancellation.**  Recompute all local rows jointly; do not
   discard a pair because one prefix fails.
9. **All frozen cores.**  Check every known occurrence-labelled q1 core,
   not only the priced `114930` fan.  An unchanged core is an exact prune.
10. **Global formula.**  After the structural filters, verify exact q1 and
    rank-ten integrality and authenticate any UNSAT proof.
11. **Separate downstream gates.**  State separately residence outside the
    local collar, topology, upper/deep shadows, chronology, and common
    compiler feasibility.

## 10. Sharp proved boundary

Proved:

* the selected-colour dependency cone is sound;
* the full authenticated protected C6 catalogue is negative;
* the complete protected star-C8 catalogue is negative;
* the 65 compatible pairs within the twelve visible clean one-recut menu
  are exact-q1 negative; and
* every unrestricted Hamming-two breaker satisfies the central / individual
  / cross-activation trichotomy.

Open:

* protected octahedral C8;
* exact owner-stable classification of the 138 conservative rows;
* pairs involving dirty recuts, central recuts, or joint-only colour
  activation;
* larger final-net alternating circuits; and
* all upper/deep/compiler gates beyond the scoped q1/rank-ten formulas.

The corrected theorem is therefore a reusable pruning theorem and a
precise enumerator specification, not a global physical-socket no-go.
