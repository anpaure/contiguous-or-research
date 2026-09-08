# A q=3 four-by-four near-C owner atom exists on eleven reduced labels

**Date:** 2026-08-14
**Status:** exact named-owner theorem with independent H100 replay.  It is
optimal in both rails per shore and reduced-ground size within the
period-eight/period-nine distance-one near-C model.  Typed q1/q2 resources,
residence and global factor topology are not claimed.

## 0. Outcome

Let the reduced ground be

\[
                 V=\{0,1,\ldots,10\},\qquad H=\{0,1,2,3\}.
\]

There are four positive and four negative q=3 cyclic rails, of periods
eight and nine, whose owner decks are simple on each shore and satisfy

\[
       \sum_{Q\in\mathcal A^+}f(Q)
       =\sum_{Q\in\mathcal A^-}f(Q)+e_H.           \tag{0.1}
\]

The positive shore has 34 distinct owners, the negative shore has 33, and
its entire owner set is the 33-owner subset of the positive shore obtained
by deleting `H`.

The preceding q3 obstruction proves that no three-by-three atom exists and
that no four-by-four atom exists on ten reduced labels.  Hence this witness
attains both lower bounds exactly.

## 1. Literal rail certificate

For a centre `c` and a cyclic word
`sigma=(s_0,...,s_(N-1))` of distinct labels avoiding `c`, write

\[
 R(c;\sigma)=
 \bigl(\{c,s_i,s_{i+1},s_{i+2}\}\bigr)_{i\in\mathbb Z_N}.    \tag{1.1}
\]

Take the positive rails

```text
p8a  centre 0:  1 2 3 10 7 5 6 8
p8b  centre 0:  1 4 2 7 5 3 9 8
p9a  centre 1:  2 6 3 7 5 10 9 4 8
p9b  centre 2:  0 1 7 5 10 6 8 3 9
```

and the negative rails

```text
n9   centre 0:  1 9 2 3 10 7 5 6 8
n8a  centre 1:  0 8 4 9 10 5 7 2
n8b  centre 2:  0 7 5 10 6 8 1 4
n8c  centre 3:  0 5 7 1 6 2 8 9.
```

Every consecutive pair of owners in `(1.1)`, including the wraparound
pair, differs by deleting one toggle label and adding one toggle label.
Thus each displayed rail is a Johnson cycle.

### Theorem 1.1 (exact owner equality and simplicity)

The eight displayed rails satisfy all of the following.

1. Each rail has as many distinct owners as its period.
2. The four positive decks are mutually disjoint, for 34 positive owners.
3. The four negative decks are mutually disjoint, for 33 negative owners.
4. The negative owner set is contained in the positive owner set.
5. Their set difference is exactly `H={0,1,2,3}`, occurring in the first
   window of `p8a`.

Consequently `(0.1)` holds as an equality of named owner occurrence
vectors, not merely after point projection.

## 2. Exact centre and support ledger

The centre profile is

```text
positive:  2 period-8 at 0;  period-9 at 1 and 2
negative:  period-9 at 0;    period-8 at 1, 2 and 3.
```

The noncentre support holes are

```text
p8a: 4,9       p8b: 6,10      p9a: 0       p9b: 4
n9:  4         n8a: 3,6       n8b: 3,9     n8c: 4,10.
```

Since a centre contributes its full period and every toggle label belongs
to exactly three cyclic windows, the signed point-degree difference is

\[
                    (1,1,1,1,0,0,0,0,0,0,0),      \tag{2.1}
\]

as required by `(0.1)`.  In particular `t_0=-2`: one positive long support
contains `0`, while all three negative short supports contain `0`.

There is one useful correction to the raw five-type centre list.  If both
positive period-nine rails had the same exterior centre `x`, then
`a_x=0,b_x=2`, so the exact point equation

\[
                      8a_x+9b_x+3t_x=0
\]

would force `t_x=-6`, contradicting `|t_x|<=4`.  Thus repeated positive
long centres are possible only at a target; “same exterior” is eliminated
before cyclic-order selection.

## 3. Common-core lift

Let `C_0` be any fixed set disjoint from `V`.  Replace every reduced owner
`Q` above by `C_0 union Q`.  Johnson adjacency, every cyclic order,
within-shore simplicity and the complete occurrence equality are preserved,
and `(0.1)` becomes

\[
 \sum_{Q\in\mathcal A^+}e_{C_0\cup Q}
 =\sum_{Q\in\mathcal A^-}e_{C_0\cup Q}+e_{C_0\cup H}.       \tag{3.1}
\]

Hence the certificate is a literal distance-one near-`C_0` owner atom at
every ambient rank for which the common core is admissible.

## 4. Independent H100 verification

The solver certificate was checked by a separate verifier that imports no
solver code.  It rebuilds every cyclic owner window, checks every Johnson
edge, rail and shore simplicity, the complete 33-owner intersection, the
single extra target owner, the centre/support profile and every point
degree.

```text
scratch/verify_q3_near_c_four_by_four_v11_atom_20260814.py
SHA-256 e975f97fc80bfb1ea424fd1bfe4b1559653cc22155e1e6c91313f17fa4b520d5

H100 output SHA-256
d9d53244fb68970b099c2897740db24d291d47e792a026c185dcf9f32c48970d
```

Exact output:

```text
PASS q=3 ground=11 positive_rails=4 negative_rails=4 positive_owners=34 negative_owners=33 common_owners=33 extra_owner=0123 shore_simple=yes rail_cycles_johnson=yes point_difference=1,1,1,1,0,0,0,0,0,0,0 rail_owner_counts=p8a:8,p8b:8,p9a:9,p9b:9,n9:9,n8a:8,n8b:8,n8c:8 auxiliary_count_histogram=0:1,1:7,2:16,3:10
```

The supporting exact-cover model separately enforces support equations,
one cyclic circuit per rail, every named owner equality and shore
simplicity:

```text
scratch/search_q3_near_c_four_by_four_v11_exact_atom_20260814.py
SHA-256 1761a4e22af242867b93e2c1efa56ebad7b3565ccb0e51433012612f77e5a829

support census output SHA-256
c43b784007033c8fead2beb1ad55272f803fa427cd41b64f2c866b3ae24082f6

two-target full certificate SHA-256
885778c354c4a7ee382dabe4f44ae8af1a760a13e6d4073e25091d0081fb05d9
```

At support level, same target, two targets, target+exterior and two
distinct exteriors are feasible, while same exterior is infeasible.  In
the full cyclic-owner census, the two-target type is feasible and the
other three surviving support types return `INFEASIBLE`.  These solver
statuses classify this normalized finite model; the positive theorem
itself rests on the literal certificate and independent replay above.

## 5. Scope

This closes the q3 **named-owner semigroup** gate for one distance-one
near-C atom.  It does not assert equality or simplicity of immediate
lower/upper colours, q2 windows, compatible owner ordering against another
factor, residence, or a connected global topology.  Those are separate
compiler obligations.
