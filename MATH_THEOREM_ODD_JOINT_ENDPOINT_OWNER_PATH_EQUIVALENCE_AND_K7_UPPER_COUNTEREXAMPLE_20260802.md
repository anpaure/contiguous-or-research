# Joint endpoint linearization: eliminate the containment matching, and a sharp `K7` upper counterexample

**Date:** 2026-08-02  
**Status:** unconditional equivalence and an exact literal `K7` counterexample.
This note concerns only the central owner path, the immediate lower palette,
the lollipop endpoints, and the immediate upper palette.  It does not impose
residence, higher upper targets, source traces, or the lower compiler, and it
does not prove `nu(17)=24313`.

## 0. Outcome

For odd `k=2r-1`, the joint choice of

\[
 (\mu,\text{ rooted Hamilton path},M,D,B,C)
\]

has an exact matching-free form.  It is simply a permutation of the rank-`r`
owners whose consecutive intersections are `W-1` distinct rank-`(r-1)`
sets, subject to three endpoint conditions.  The containment matching is
then uniquely reconstructed; it is not a further decision variable.

This reduction makes it possible to test the first nonautomatic upper case
directly.  At `K7` there is a joint fixed-boundary lollipop path with all
owners once and all but one lower colour once, but with only `19/21`
immediate upper colours.  Consequently

\[
 \boxed{\text{joint feasibility of }\mu\text{ and the lollipop endpoints}
        \not\Longrightarrow q1\text{ upper surjectivity}.}
\]

The `K5` automatic-upper theorem is therefore sharp: automaticity already
fails at `K7`.

## 1. Eliminate `mu`

Put

\[
 \mathcal Q={{[2r-1]}\choose{r-1}},\qquad
 \mathcal T={{[2r-1]}\choose r},\qquad
 W=|\mathcal Q|=|\mathcal T|.
\]

### Theorem 1.1 (joint matching--path elimination)

The following two data sets are in bijection.

**Root-link data.**

* a perfect containment matching
  \(\mu:\mathcal Q\to\mathcal T\);
* a directed Hamilton path
  \(L_0\to L_1\to\cdots\to L_{W-1}\) in its root-link digraph;
* the owner word \(T_i=\mu(L_i)\);
* terminal root and owner \(M=L_{W-1}\), \(B=T_{W-1}\), and initial
  owner \(C=T_0\);
* adjacent endpoints with
  \[
             D=B\cap C,\qquad D\ne M,\qquad D\ne L_0.
  \tag{1.1}
  \]

**Direct owner-path data.**

A permutation

\[
                         T_0,T_1,\ldots,T_{W-1}
\tag{1.2}
\]

of `mathcal T` such that

1. consecutive owners are Johnson adjacent;
2. the intersections
   \[
                  q_i=T_i\cap T_{i+1}\quad(0\le i<W-1)
   \tag{1.3}
   \]
   are pairwise distinct;
3. the unique omitted member
   \(M\in\mathcal Q\setminus\{q_0,\ldots,q_{W-2}\}\) satisfies
   \[
                              M\subset T_{W-1};
   \tag{1.4}
   \]
4. the endpoints are Johnson adjacent and, with
   \[
             C=T_0,\qquad B=T_{W-1},\qquad D=B\cap C,
   \tag{1.5}
   \]
   one has
   \[
                              D\ne M,\qquad D\ne q_0.
   \tag{1.6}
   \]

The inverse map from (1.2)--(1.6) is unique:

\[
 \boxed{
   \mu(q_i)=T_i\ (0\le i<W-1),\qquad
   \mu(M)=T_{W-1}.}
\tag{1.7}
\]

#### Proof

Start with the root-link data.  The contracted-path identity gives

\[
                         T_i\cap T_{i+1}=L_i
                         \quad(0\le i<W-1).
\tag{1.8}
\]

The `L_i` are distinct because the root path is Hamiltonian.  Its only root
not used as an owner adjacency is its terminal root `M`, and
`M subset mu(M)=B`.  The fixed-boundary hypotheses are exactly
(1.5)--(1.6).  Thus (1.2)--(1.6) follow.

Conversely assume the direct owner-path data and define `mu` by (1.7).
The `q_i` together with `M` are every root exactly once, while the images in
(1.7) are every owner exactly once.  Every assigned root is contained in
its owner, so `mu` is a perfect containment matching.

Put

\[
 L_i=q_i\quad(0\le i<W-1),\qquad L_{W-1}=M.
\]

For `i<W-2`,

\[
 L_i=q_i\subset T_{i+1}=\mu(q_{i+1})=\mu(L_{i+1}),
\]

and the same calculation at the last arc gives

\[
 L_{W-2}=q_{W-2}\subset T_{W-1}=\mu(M).
\]

Distinctness makes all these nonmatching root-link arcs.  Hence the `L_i`
form the required directed Hamilton path.  Conditions (1.5)--(1.6) are
exactly the fixed-boundary closure conditions.  Formula (1.7) also proves
uniqueness.  \(\square\)

### Corollary 1.2 (direct immediate-upper gate)

Under Theorem 1.1, immediate-upper surjectivity is exactly

\[
 \left\{T_i\cup T_{i+1}:0\le i<W-1\right\}
       ={{[2r-1]}\choose{r+1}}.
\tag{1.9}
\]

Thus the genuinely joint central problem is a **near-rainbow Johnson owner
path with a rooted endpoint closure**, plus (1.9).  Neither `mu` nor the
alternating incidence word needs to appear in an exact selector.

## 2. A literal `K7` counterexample

Take `r=4`, `k=7`, `W=35`, and use decimal bit masks on coordinates
`0,...,6`.  The owner path is

```text
113,57,105,75,78,108,45,53,60,58,43,27,90,92,30,54,51,39,
15,46,102,101,99,83,23,85,89,29,77,71,86,116,120,106,114.
```

Every entry has rank four and the 35 entries are all the rank-four owners.
Every consecutive pair is Johnson adjacent.  Its 34 intersections are
pairwise distinct, with unique missing root

\[
                              M=82.
\tag{2.1}
\]

The endpoint data are

\[
 C=113,\qquad B=114,\qquad D=C\cap B=112,
 \qquad q_0=113\cap57=49.
\tag{2.2}
\]

They obey

\[
 M\subset B,\qquad D\ne M,\qquad D\ne q_0.
\tag{2.3}
\]

Theorem 1.1 therefore reconstructs a genuine perfect containment matching
and the required fixed-boundary root-link Hamilton path.

Nevertheless its consecutive unions contain only 19 of the 21 rank-five
sets.  The two absent upper colours are

\[
                              31\quad\text{and}\quad117.
\tag{2.4}
\]

This proves the promised counterexample.

For reproducibility, the reconstructed matching is

```text
7:39,11:43,13:29,14:15,19:83,21:23,22:30,25:89,26:27,28:92,
35:51,37:45,38:46,41:57,42:58,44:108,49:113,50:54,52:53,
56:60,67:99,69:77,70:71,73:105,74:75,76:78,81:85,82:114,
84:86,88:90,97:101,98:106,100:102,104:120,112:116.
```

Here each entry is `root:owner`.  In particular, this is not a failure
caused by freezing a hostile matching first: the matching, path, missing
root, duplicated root, and endpoints were selected simultaneously.

## 3. Exact bounded census model

The witness was found by a compact direct CNF generated and decoded by

```text
scratch/build_audit_k7_joint_endpoint_missing_upper_20260802.cpp
```

The model has variables for the owner at every path position, the lower
colour at every adjacency, and the used-root indicators.  Its clauses
enforce, literally:

* one copy of every owner;
* Johnson adjacency;
* 34 pairwise distinct lower colours;
* the omitted root is contained in the terminal owner;
* adjacent endpoints and the two inequalities in (1.6);
* absence of the normalized upper colour `31`.

The last normalization is lossless under `S_7`: any missing rank-five
colour can be relabelled to `31`.  The generated instance has

```text
variables  2450
clauses    127904
```

and Kissat returns `SAT`.  A second, independent `O3` C++ replay uses only
the 35 owner masks above:

```text
scratch/audit_k7_joint_endpoint_missing_upper_witness_20260802.cpp
```

It independently reconstructs `mu`, checks every root-link arc, replays the
fixed boundary and both missing upper colours, and verifies the `r=4`
external-chord identity for every rank-five target.

Authoritative H100 root:

```text
/home/amodo/or15/work/root_joint_endpoint_linearization_20260802
```

Authenticated results:

```text
builder/decoder source SHA-256
  4d47c4086427acac473ffe5c0abcde72eb6b38618bfbafc2680a43b480e3c1db

builder/decoder O3 binary SHA-256
  ad5ed1f89218cfaf48adba1a4e1e1a3bbb1b3d15325c370e0a98a1c154ffb1d9

CNF SHA-256
  8dc97ec0e622a93c6c4735bba762e782f18fa17f0ef2a9875f8398e7c8f87b71

SAT model SHA-256
  a9a4d3e09e53f2f682610e7dfae7bb47c5d01593bc3d79cb27c3ebdde63f2904

decoder replay SHA-256
  a5bf2e1c4ade29535dd7eff8f7784cd06b37f34b79884f0cb456e98a01673d20
```

The final independent-audit source/output hashes are recorded in the remote
root after recompilation of the displayed source:

```text
independent audit source SHA-256
  68f1702595988651a90ae4c3ae48bce23ef8aaef0376f53eb43406cf629789bd

independent O3 binary SHA-256
  746e9595e0b8af8a00d4830815a524b8bd0321d77be93856fdd950646b490fc2

independent replay output SHA-256
  1d505e1f5da9eb0682f95738125dd7e885cbc12fcd58d17dacf2652100b2aae0
```

The replay also gives the two exact threshold failures:

```text
U=31   u=0  g=0  a=0  m=0
U=117  u=0  g=1  a=1  m=0
```

## 4. Consequence and exact remaining theorem

The matching-elimination theorem removes a large artificial layer from the
joint selector.  But the `K7` witness proves that the immediate upper row
cannot be deleted with it.  The correct central target is precisely:

> Construct a permutation of all rank-`r` owners satisfying
> (1.3)--(1.6) and the upper-union equation (1.9).

Equivalently, using the external-chord identity from the companion root-link
note, choose the direct path so that every upper external load reaches its
pointwise threshold.  At `K7`, the two missing colours in (2.4) are literal
threshold failures; from `K7` onward the q1 upper distribution is an
independent correlated design condition.

This note does not decide whether the direct target exists for every `r`.
It proves that any all-`r` construction must build upper balance jointly
with the near-rainbow endpoint path rather than infer it afterward.
