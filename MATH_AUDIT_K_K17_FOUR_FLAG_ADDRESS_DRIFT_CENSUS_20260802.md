# Independent K17 four-flag address-drift census

**Date:** 2026-08-02  
**Lane:** protected Catalan/pivot, independent finite audit  
**Status:** exact projection census on the frozen K17 chain table.  This note
does not assert a state-consistent cycle cover, residence, an upper deck, a
source cap, a compiler, or a word.

## 1. Verdict

The strict lower triangle of the complete long-row four-flag role-pair matrix
is exactly zero.  In the address order

\[
  0=12/1,\qquad 1=12/2,\qquad 2=23/2,\qquad 3=23/3,
\]

the independently reconstructed matrix into the `18,646` hard long heads is

\[
\boxed{
\begin{pmatrix}
4827&4407&5770&14488\\
0&1196&2295&5668\\
0&0&1276&4528\\
0&0&0&4738
\end{pmatrix}.}
\]

There are `49,193` distinct compatible role pairs.  Every compatible role
pair belongs to exactly one of the ten displayed flag-pair classes; no pair
has two different flag witnesses.  There are no self transitions.  Including
the seventeen bottom-rank-one long heads changes the matrix only to

\[
\begin{pmatrix}
4827&4408&5771&14490\\
0&1196&2295&5669\\
0&0&1276&4529\\
0&0&0&4739
\end{pmatrix},
\]

with `49,200` distinct role pairs.

The first producer's numeric matrix is therefore correct.  The independent
enumerator does not reuse its `intervals_intersect` predicate: it merges the
four literal cells after imposing the two shift equalities, intersects the
entering cell with `[T-U,T]`, checks every lower/upper interval, and emits a
concrete four-cell witness for every accepted flag pair.  For short rows it
also rechecks the exact prescribed cell-union constraint after all merges.

## 2. Long matching and exact threshold demand of the frozen witness

The union of the ten long-to-hard classes has maximum matching `14,844`, so
its hard-head deficiency is

\[
                     18,646-14,844=3,802.
\]

An alternating-reachability Hall witness has `4,605` hard heads and only
`803` long suppliers, giving the same deficiency `3,802` in one exact cut.
The four constant-flag diagonal matching numbers are

\[
                  (4601,1195,1178,2167).
\]

The frozen producer matching has `14,844` rows, distinct suppliers and
distinct hard heads.  Every mask is a singleton and is present in the
independent witness file.  Its ten class counts are

\[
\begin{array}{c|rrrrrrrrrr}
(\alpha,\beta)&00&01&02&03&11&12&13&22&23&33\\ \hline
\#&3608&2288&1472&2860&671&612&1059&341&938&995.
\end{array}
\]

For threshold `t=1,2,3`, let

\[
 D_t=\#\{e:\alpha(e)<t\leq\beta(e)\}.
\]

Direct recomputation gives

\[
\begin{aligned}
D_1&=2288+1472+2860=6620,\\
D_2&=1472+2860+612+1059=6003,\\
D_3&=2860+1059+938=4857.
\end{aligned}
\]

Thus the frozen witness has

\[
                   \boxed{D=(6620,6003,4857),\quad\rho=6620>5647.}
\]

This is the exact reset demand of that witness, not an optimum over all
maximum long projections.  A one-worker optimization of `rho` was stopped on
request before producing a certificate, so the minimum possible `rho` remains
**unknown** in this audit.

## 3. Short-row projection and Hall cut

The table contains `5,647` short roles: `1,748` length-one and `3,899`
length-two.  Their exact outgoing role-pair neighborhoods into hard long heads
have

\[
                 5,764\quad\text{and}\quad15,895
\]

edges respectively.  In the reverse direction, all long rows into short
rows have `5,682` and `15,898` role-pair edges respectively.  The outgoing
counts reproduce the earlier producer exactly.

Adding all short suppliers to all long suppliers raises the maximum hard-head
matching to

\[
                         18,115,
\]

but still leaves exact deficiency `531`.  An explicit Hall witness has `729`
hard heads and `198` suppliers, split as

\[
        8\text{ length-one}+148\text{ length-two}+42\text{ long}.
\]

Among all matchings of the maximum size `18,115`, the least possible number
of short-to-hard arcs is exactly `3,271`.  This was checked by binary search on
a short-supplier capacity followed by an exact integral max flow.  It is not a
full-cover number: a cover of all `18,646` hard heads does not exist on this
projection.

## 4. One-short correlated reset sockets

The audit also intersects both sides of a single physical short state.  A
record `(j,s,i,alpha,q,beta)` is retained only when one state of short role
`s`, at its address `q`, simultaneously supports

\[
             (j,\alpha)\longrightarrow(s,q)\longrightarrow(i,\beta).
\]

There are `18,791` such endpoint/flag/address records.  The number of short
roles supporting each ordered long-flag pair is

\[
\begin{pmatrix}
547&1097&1011&2053\\
177&387&356&819\\
60&112&244&536\\
0&56&121&280
\end{pmatrix}.
\]

These entries overlap because one short role may support several pairs.
Exactly `445` short roles support at least one strict reset
`alpha>beta`; there are `677` concrete strict-reset records.  In particular,
no single short role supports a direct `3 -> 0` reset between long endpoints.
There are `627` short roles with no incoming long neighbor, `85` with no
outgoing long neighbor, and `2,162` with no correlated one-short socket at
all.

This is a one-short calculation only.  It neither rules out nor counts reset
paths using two or more consecutive short roles or an enriched macro.

## 5. Frozen artifacts

The persistent H100 root is

```text
/home/amodo/or15/work/k_fourflag_audit_20260802
```

The local mirror is

```text
scratch/k_fourflag_audit_20260802
```

Principal SHA-256 values are:

```text
table
029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1

independent C++ source
8869cfb812a56567ef2b47c55d1ad5b7a29c00963daad88b4ca38682401832a9

audit JSON
833161e9c666473cd2f7b1d1a4022756d3382f70e9ee0955b41b2457c8b3cab5

long four-cell witnesses
fe5aa600067494711fb77fe9cb944855d47cf5c38702667238af8f2cb35c1d07

short-to-hard neighborhoods
0337c0a07cf78de2080cd7d0f216881553b4b2df347f466564a5dee8e31f09e8

long-to-short neighborhoods
d1ad7b9ee5d4868660ea872d32bb410f4872377cd10ec0996396b25799c5c921

one-short socket summary
4749d627cb167caa8820e5c0dc584af7c8ce6bb456566d112a117968e76ae30d

one-short reset records
6b9f6c5264f939bce1c5217f38372fd01bcbec1be9d03cfa6c5e1c863f64e15a

Hall head sets
d485aeaa4a2728052fc28261ed1c71abad25c3d0d3723b02d2785a35930674e8

producer long matching independently replayed here
190a5ca2f9f5dccf590196c42264d3edf18c2ea4e5f02b173ed9e73ead4cfaae
```

The H100 run used one pinned CPU, `41.26` user seconds, `1:22.76` elapsed,
and `24,372 KiB` peak RSS.  The source asserts the row census, all table
ranks and containments, the absence of lower-triangular and self transitions,
and every emitted matching/witness cardinality.
