# Audit of the clean-package tight-wreath-row identity

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_CLEAN_FACET_PACKAGE_IS_FOUR_ARCS_OF_ONE_TIGHT_WREATH_ROW_20260813.md`  
**Source SHA-256:**
`da9b55dfb0cfbebfe8dd5b5e5c2b8ceefc6b14e8990447d7d85cc000cd6f6927`  
**Method:** literal cyclic-window index arithmetic; no computation or
search.  
**Verdict:** **PASS.**  The current Theorem 3.1 now states the exact count:
the four halo arms are the four displayed arcs, while the whole protected
package is those arms plus two central paths, equivalently two collared row
blocks.

The requested preliminary SHA `b1e0f719...`, and the first audited SHA
`bf699543...`, were earlier versions.  The current delta adds the symbolic
window-shift proof, normalizes the arc-count wording, and records a finite
identity replay.  It changes none of the audited set identities or scope.

## 1. Central antipodes

In zero-based positions, the order (1.4) has blocks

\[
 D:[0,q-1],\quad C:[q,m-1],\quad
 I:[m,m+q-1],\quad S:[m+q,2m].                    \tag{1.1}
\]

Thus `L_0=D union C` and shifting `L_(t-1)` to `L_t` deletes `d_t`
and inserts `i_t`, exactly recovering the clean facet geodesic.  The
complement of the length-`m` window beginning at `t` is the length-`m+1`
window beginning at `t+m`, hence

\[
                         \overline{L_t}=A_{m+t+1}.         \tag{1.2}
\]

The complement of the `A_t` window beginning at `t-1` begins at `t+m`,
so

\[
                         \overline{A_t}=L_{m+t}.           \tag{1.3}
\]

Equations (2.1)--(2.5), including every one-unit index shift, are correct.

## 2. The four literal halo arms

Starting from the left upper-path endpoint `A_1` and moving backward to
`A_(-d)` makes `d+1` exchanges.  It deletes first `i_1` and then

\[
 c_{m-d-q+1},\ldots,c_{m-q},                              \tag{2.1}
\]

and inserts the last `d+1` elements of `S`.  This is exactly the forced
first deletion plus `K^-` and `J^-` in (3.2).

Moving forward from `A_q` to `A_(q+d+1)` deletes first `d_q` and then
`c_1,...,c_d`, while inserting `s_1,...,s_(d+1)`.  This is (3.3).

The antipodal intersection arms are equally exact:

* `A_(m+1)` backward to `A_(m-d)` deletes the last `d+1` members of `S`
  and inserts `c_(m-d-q),...,c_(m-q)`;
* `A_(m+q+1)` forward to `A_(m+q+d+2)` deletes
  `s_1,...,s_(d+1)` and inserts `c_1,...,c_(d+1)`.

These are precisely the banks in (3.1).  Their sizes are respectively
`d+1`; the upper-path auxiliary `K` banks have size `d`.  Under

\[
                         m=R-1\geq3d+2,
 \qquad                  q\leq d,                         \tag{2.2}
\]

all displayed indices are in range, and the left and right banks within
each coordinate block are disjoint.  No endpoint resource has silently
been reused.

## 3. Equality case `R=3d+3`

The two collared owner-index blocks are

\[
 B_0=[-d,q+d+1],
 \qquad
 B_1=[m-d,m+q+d+2]\pmod{2m+1}.                            \tag{3.1}
\]

In each cyclic direction the number of owner indices strictly between
them is

\[
                         g=m-q-2d-2.                       \tag{3.2}
\]

Condition (2.2) gives `g>=0`.  At the sharp equality

\[
                         R=3d+3,
 \qquad m=3d+2,
 \qquad q=d,                                               \tag{3.3}
\]

one has `g=0`: the end owner of one block and the start owner of the other
are consecutive, not equal.  The two block sizes are

\[
 |B_0|=3d+2,
 \qquad |B_1|=3d+3,                                       \tag{3.4}
\]

and sum to `2m+1=6d+5`; they partition the row owners.  Facets internal to
one block lie between two owners of that block.  The two facets joining
the consecutive far-port pairs are the only boundary facets and belong to
neither protected halo.  Therefore owner and lower-facet resource
disjointness remains exact at equality.

## 4. Scope

The local row representation and isolated-row extension consequence are
valid.  They imply no hereditary simultaneous extension theorem.  The
separate two-row obstruction is therefore logically compatible with this
note.

The current literal phrasing of Theorem 3.1 is exactly

\[
 \text{two central arcs plus four halo arms}
 \quad\Longleftrightarrow\quad
 \text{two collared arcs of one tight row}.               \tag{4.1}
\]

That count clarification changes no set identity or consequence.
