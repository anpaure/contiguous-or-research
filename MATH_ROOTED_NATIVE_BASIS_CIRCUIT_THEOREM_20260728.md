# Rooted native-basis circuits and the exact next Hall descent

Date: 2026-07-28

Status: graph theorem plus an exact, search-free audit of the canonical
Hall-21 carrier.  This note does **not** claim Hall 20, a common compiler for
a full matching, or a length-6438 covering word.

## 1. The abstract circuit

Let `G=(L,R,E)` be an occurrence-labelled compiler graph.  Fix one physical
controller word `Q`; for a cell `c in R`, write `tr_Q(c)` for the OR of `Q`
on that cell interval.

### Definition 1.1 (rooted native-basis circuit)

A connected induced pair `(X,Y)`, with `X subset L` and `Y subset R`, is a
rooted native-basis circuit with root `rho` if

1. `|X|=|Y|+1`;
2. `rho in X`;
3. `c -> tr_Q(c)` is a bijection from `Y` to `X\{rho}`; and
4. every pair `(tr_Q(c),c)` is an edge of `G`.

The word *native* refers to using one common controller `Q`, not to choosing
an independently thinned word for each cell.

### Lemma 1.2 (basis matching)

Every rooted native-basis circuit has matching rank `|Y|`; its displayed
native edges form a matching which saturates `Y` and leaves exactly `rho`
unmatched in `X`.

This is immediate from the bijection in Definition 1.1.  The content in an
application is proving that all native traces are distinct and omit only one
target.

### Theorem 1.3 (duplicate-child/root split)

Assume `(X,Y,rho)` is a rooted native-basis circuit under `Q`.  Let `a` be
one target in `X\{rho}`, and let `c_a` be its native cell.  Suppose a legal
endpoint supplies a second physical cell `c'_a != c_a` and one common word
`Q'` such that

* `tr_{Q'}(c'_a)=a`;
* `tr_{Q'}(c_a)=rho`;
* every other old basis cell `c in Y\{c_a}` still has
  `tr_{Q'}(c)=tr_Q(c)`; and
* all these cells are distinct from an exterior matching of the required
  rank.

Then the endpoint matches every target of `X`: use `c_a` for `rho`, `c'_a`
for `a`, and retain all other native basis edges.  Relative to the old
circuit, the matching rank rises by one.  If the exterior matching has rank
`nu-(|X|-1)`, where `nu` is the old global matching rank, then the new global
rank is at least `nu+1`.

The proof is the displayed union of pairwise disjoint physical edges.  This
formulation separates three facts which a scalar Hall calculation conflates:

1. a duplicate child exists;
2. one copy can be redirected to the root in the **same** word; and
3. the exterior matching survives disjointly.

### Corollary 1.4 (neutral compression is physical, not numerical)

Replacing a rooted `s/(s-1)` circuit by a rooted `t/(t-1)` circuit while
preserving global rank does not itself improve Hall deficiency.  Its value is
that Theorem 1.3 then has to control only `t-1` old basis cells.  The certified
Hall-22 route realizes exactly this pattern:

```text
160/159 rooted circuit -> 24/23 rooted circuit -> discharged circuit.
```

The first arrow is matching-neutral; the second creates a duplicate native
child and redirects one copy to the exposed root.

## 2. Exact Hall-21 normal form

For

```text
scratch/k15_segment_braid_hall21_zero6.json
```

the canonical Dulmage--Mendelsohn shore has `846` targets and `825` physical
cells.  Exact reconstruction decomposes it into 21 connected components:

| type | roots |
|---|---|
| `169/168` | `1920` |
| `161/160` | `960, 8217, 24610` |
| `160/159` | `8218` |
| `5/4` | `4213, 7504` |
| `3/2` | `1103, 18970` |
| `2/1` | `2420, 2575, 2676, 9524, 17683, 19568` |
| `1/0` | `5801, 13616, 13620, 17738, 21641, 29776` |

Every component is a rooted native-basis circuit under the one maximal
erosion controller.  Concretely, if `X` is the target set of a component,
then its root is

```text
rho = intersection of all targets in X,
```

and the native traces of its right cells are pairwise distinct and equal
exactly to `X\{rho}`.  Thus the Hall deficiency 21 is not diffuse: it is the
sum of 21 literal exposed roots.

The 825 native shore pins extend as incidence edges to a global matching of
rank

```text
825 + 15537 = 16362.
```

This last equality does not assert that the 15,537 exterior edges are all
realized by the same maximal word; it is an incidence-rank statement.

## 3. Exact socket census

The frozen Hall-21 word has two useful families of root redirections.

1. The five large rank-four-root components have 45 depth-zero native atom
   cells (nine per component) which can individually be shrunk from the atom
   to the root while preserving every central window and every other native
   shore pin.
2. Each of the six `2/1` components has a depth-two native child cell which
   can be rebased to its rank-six root while preserving every central window
   and every other native shore pin.

In all 51 cases, however, the relevant native child has exactly one native
occurrence in the entire current cell bank.  Redirecting it immediately would
merely exchange which target is exposed.  Therefore:

> A monotone Hall-21 to Hall-20 descent in this normal form must first create
> a second native occurrence of one of the 51 socket children (or replace the
> basis by a different simultaneous pin family), and only then perform the
> root redirection.

This is the exact mathematical search objective.  It explains why the
exhaustive one-braid census can have thousands of Hall-neutral carriers but
no Hall-20 endpoint: a neutral move is useful only when it creates a physical
duplicate compatible with a subsequent common-word split.

## 4. Reproducibility

The audit is lightweight and search-free:

```bash
python3 scratch/audit_k15_h21_dm_components.py \
  --output scratch/audit_k15_h21_dm_components.json
```

It verifies:

* the exact `846/825` shore and all 21 component sizes;
* `native traces = component targets minus root` in every component;
* pairwise distinctness of all 825 native targets;
* exterior rank 15,537 after reserving those native pins;
* all 45 safe depth-zero atom-to-root ports;
* all six safe depth-two child-to-root rebases; and
* uniqueness of the native child occurrence in every audited socket.

The separate exact Hall-22 to Hall-21 common-word example is recorded in
`MATH_K15_H22_TO_H21_REMOTE_COMPONENT_COMPRESSION_20260728.md`.

## 5. The next finite theorem

For any one of the 21 rooted circuits, find a protected neutral carrier move
which either

1. creates a second native occurrence of a certified socket child, or
2. compresses the circuit to a smaller rooted native-basis circuit possessing
   such a duplicate,

and then prove that one splitter realizes Theorem 1.3 while preserving six
zero-candidate control and the exterior matching.  This is strictly sharper
than asking for a generic Hall-improving braid and is the criterion used to
rank the Hall-21 neutral beam.
