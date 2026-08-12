# K17 PBBS/Pascal incidence: Tucker triangles and exact cycle-cut intervalization

Date: 2026-07-31  
Status: exact marginal incidence theorem and authenticated finite audit  
Scope: the `AA`, `X`, and `Y` Pascal shores of the frozen PBBS
`longrun2-final` lower-`q_1` factor; common-cap trace guards and a K17 word
are not asserted

## 0. Result

No authenticated **physical** K17 lower-target/common-cap incidence graph
currently exists for this PBBS carrier: there is not yet a final connected
chronology together with a legal staircase and its capped maximal envelopes.
It would therefore be unsound to claim a consecutive-ones verdict for that
not-yet-defined graph.  The strongest frozen residual object is instead the
exact lower-`q_1` Pascal factor below.  Its complete active
Boolean-inclusion banks are the relevant marginal relaxation, and its
selected support is literal.

There is no ordering of the active Pascal owner cells which makes every
neighbourhood in the **complete** one-bit-extension banks an interval.  Each
of the three frozen shores contains the inclusion-minimal Tucker matrix

\[
 M_I(3)=
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix}.
\tag{0.1}
\]

The already selected factor support is much closer to interval-convex.  It
has maximum degree two.  Its exact cyclic-component counts are

\[
\begin{array}{c|r|r|r|l}
\text{shore}&\text{targets}&\text{owners}&\text{components}
 &\text{cycle target-lengths}\\ \hline
AA&5005&5005&5&8,26,232,1386,3353\\
X &5720&5720&715&\varnothing\\
Y &5720&5720&716&8.
\end{array}
\tag{0.2}
\]

Consequently the selected `X` support already has a consecutive-ones
owner order.  The selected `AA` and `Y` supports require exactly five and
one incidence deletions, respectively.  Canonical cuts and explicit audited
column orders are frozen below.  This gives a precise guard-design target,
not a common-cap compiler: a proposed trace guard must perform these cycle
hits while retaining the physical trace equations and the coupled Hall
conditions.

## 1. Universal Pascal Tucker triangle

Let `K` be an `(r-1)`-set and let `a,b,c` be distinct elements outside
`K`.  In the rank-`r` to rank-`(r+1)` inclusion matrix take target rows

\[
 K+a,\quad K+b,\quad K+c
\]

and owner columns

\[
 K+a+b,\quad K+a+c,\quad K+b+c.
\]

The induced matrix is (0.1).  If all three row supports were intervals in a
linear column order, all three unordered pairs of the three displayed
columns would have to be adjacent.  A linear order of three objects has only
two adjacent pairs.  Thus no such order exists.

The obstruction is inclusion-minimal.  Deleting any row leaves only two
adjacency requirements and deleting any column leaves only two columns; in
either case a consecutive-ones order exists.  This is Tucker's
`M_I(3)`, proved here directly without invoking a recognition algorithm.

The point is structural: any unpruned PBBS/Pascal bank which retains all six
one-bit incidences around one such three-extension star fails the convex-bank
hypothesis of the guarded-convex compiler theorem.  Reordering by colex,
lexicographic, PBBS orbit, Pascal sector, or deadline cannot remove this
hereditary submatrix.

## 2. Literal frozen obstructions

The authenticated source is

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_longrun2_final_20260731.tsv
SHA-256 f0bcf846a295ed7bf8f622c873616de12eb6ba8e077dca60022d75be7ae38292
```

with factor audit SHA-256

```text
bfdb91e4874575e54a2977365e6aba1c9b8cc65b0ee3c6683702e10af356f80d.
```

On the active row and owner vertices, the complete Pascal banks have the
following sizes and first literal Tucker triangles.

### `AA`: rank six to rank seven

There are 5005 target rows, 5005 owner columns, and 35035
one-bit-extension incidences.  With core `0x001f` and exterior bits
`5,6,7`, use

```text
targets  0x003f  0x005f  0x009f
owners   0x007f  0x00bf  0x00df
matrix   110     101     011
```

### `X`: rank seven to rank eight

There are 5720 active target rows, 5720 active owner columns, and
41323 incidences.  With core `0x003f` and exterior bits `6,7,8`, use

```text
targets  0x007f  0x00bf  0x013f
owners   0x00ff  0x017f  0x01bf
matrix   110     101     011
```

### `Y`: rank seven to rank eight

There are 5720 active target rows, 5720 active owner columns, and
41336 incidences.  With core `0x003f` and exterior bits `6,8,9`, use

```text
targets  0x007f  0x013f  0x023f
owners   0x017f  0x027f  0x033f
matrix   110     101     011
```

The audit tests all six column orders in each case, finds zero valid orders,
and constructs a consecutive-ones order after every possible single row or
column deletion.

## 3. Degree-two cycle theorem

Let `H=(R,C;E)` be bipartite with every vertex of degree at most two.
For each degree-two row `u` in `R`, regard its two column neighbours as an
unordered adjacency requirement.

### Theorem 3.1

The row neighbourhoods of `H` have the consecutive-ones property if and
only if `H` has no cyclic component.

#### Proof

If a component is an alternating cycle on `q` rows and `q` columns,
its `q` degree-two rows require all `q` consecutive pairs of a cyclic
order on those columns.  Restricting any proposed global linear order to
the `q` cycle columns leaves only `q-1` adjacent pairs, a contradiction.

Conversely, an acyclic maximum-degree-two component is a path.  Walk the
path and record its columns in encounter order.  Each degree-two row lies
between two consecutive recorded columns, and each degree-one row has a
singleton neighbourhood.  Concatenate these orders over components.
Every row neighbourhood is then an interval.  \(\square\)

### Corollary 3.2

For vertex-disjoint cyclic components, the minimum number of incidence
deletions which makes `H` row-convex is exactly the number of cyclic
components.  At least one edge per cycle is necessary.  Deleting one edge
per cycle turns every cycle into a path and never empties a row, proving
sufficiency.

This theorem also explains the exact selected-support obstruction: each
cycle is a Tucker `M_I(q)`.  The smallest selected `AA` obstruction is
the following `q=8` cycle:

```text
0x40e3 : 0x40e7 -- 0x41e3
0x41e2 : 0x41e3 -- 0x43e2
0x43e0 : 0x43e2 -- 0x47e0
0x46e0 : 0x47e0 -- 0x46e4
0x4664 : 0x46e4 -- 0x4666
0x4266 : 0x4666 -- 0x42e6
0x42c6 : 0x42e6 -- 0x42c7
0x40c7 : 0x42c7 -- 0x40e7.
```

The selected `Y` support has one `q=8` cycle:

```text
0x51e4 : 0x51e5 -- 0x51ec
0x51ac : 0x51ec -- 0x71ac
0x712c : 0x71ac -- 0x712e
0x702e : 0x712e -- 0x702f
0x702b : 0x702f -- 0x70ab
0x70a9 : 0x70ab -- 0x70e9
0x70e1 : 0x70e9 -- 0x70e5
0x50e5 : 0x70e5 -- 0x51e5.
```

## 4. Exact marginal intervalization

The audit deletes the lexicographically least incidence of every cyclic
component.  Its canonical cuts are

```text
AA  (0x40c7,0x40e7) (0x059c,0x259c) (0x00d7,0x02d7)
    (0x003f,0x007f) (0x005f,0x085f)
X   none
Y   (0x50e5,0x51e5).
```

Every target retains at least one incidence.  Walking the resulting paths
gives literal consecutive-ones column orders with hashes

```text
AA  8e864f71933b3257219d16e872e8c3bfee3472524cf24b72da6826014f4fe55d
X   b55ca550424080dc6da865536fda888373a95b647a199bfcf9ca1583676169be
Y   5c20940e1009d68e4b059e12fcc032707ebb8fed9f8a7582a0460583b3964abd.
```

The `AA` components are all balanced cycles, so after one cut apiece the
five alternating paths retain a unique target-saturating matching.  The
`X` and `Y` supports must not be mistaken for independent Hall systems:
their path-component balance census is

```text
       balanced   target-surplus   owner-surplus
X          391          162              162
Y          370          173              173.
```

Those shores are coupled to the other factor resources; interval order alone
does not supply their separate matchings.

## 5. Consequence for the common-cap programme

The marginal matching matrix remains totally unimodular for every bipartite
graph.  The present obstruction is more specific: the full Pascal inclusion
bank cannot use the interval-Hall/earliest-deadline specialization of the
guarded-convex theorem.

A noncircular trace-guarded subbank must hit every displayed `M_I(3)`, and
on the selected degree-two support it must hit at least the five `AA` and
one `Y` cyclic components.  The canonical cycle cuts prove that this is
enough for **marginal** intervalization.  What remains unproved is exactly
the physical condition: whether one can choose these hits so that all point,
protected-row, and selected-lower trace guards survive simultaneously with
the coupled Hall assignment.  Taking a final matching itself as the guarded
subbank would be circular and is not claimed here.

## 6. Audit artifacts

```text
scratch/audit_k17_pbbs_pascal_tucker_cycle_intervalization_20260731.py
scratch/k17_pbbs_pascal_tucker_cycle_intervalization_20260731.audit.json
```

The audit reconstructs all active vertices, verifies every selected edge is
a literal one-bit inclusion, counts the complete active banks, searches the
first Tucker triangles, checks their minimality, decomposes the selected
supports, proves the cycle-cut lower and upper counts constructively, emits
the canonical cuts, and rechecks every row against the resulting orders.
