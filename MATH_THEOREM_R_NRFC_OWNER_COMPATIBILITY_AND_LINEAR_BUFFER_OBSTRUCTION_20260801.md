# NRFC owner compatibility and the sharp linear-buffer obstruction

Date: 2026-08-01  
Lane: R, integral sequel to the aggregate monotone-rotor theorem  
Status: exact theorem.  It gives the clean labelled compatibility counts,
the exact one-copy factor Hall system after a state transversal is chosen,
and an infinite obstruction to any dimension-independent local
bounded-multiplicity conversion.  It does **not** refute the global NRFC
problem for the canonical Ferrers inventory, because globally one may pool
at least `d+1` occurrences from the large buffer banks.

## 1. Literal age states

Fix integers

```text
k>=r>d>=1.
```

For a positive age type `c=(c_0,...,c_d)`, `sum c_i=r`, let
`Omega_c(k)` be the set of ordered pairwise-disjoint tuples

```text
P=(C_0,...,C_d),       |C_i|=c_i,
```

with owner `o(P)=C_0 dotunion ... dotunion C_d`.
For `P in Omega_c(k)` and `P' in Omega_c'(k)`, write `P->P'` when

```text
C'_(i+1)=C_i-C'_0                    (0<=i<d).       (1.1)
```

This is the literal shift recurrence.  In particular

```text
o(P')=C'_0 union (o(P)-C_d).                            (1.2)
```

Put `e_i=c_i-c'_(i+1)`.  Type compatibility means `e_i>=0` for every
`i<d`.

## 2. Exact labelled compatibility counts

### Theorem 2.1 (global biregularity and owner-distance fibres)

For compatible positive types `c,c'`, the directed graph
`Omega_c(k)->Omega_c'(k)` defined by (1.1) is biregular.  Its source and
target degrees are

```text
D^+_k(c,c')
 = [prod_(i<d) C(c_i,c'_(i+1))] C(k-r+c_d,c_d),       (2.1)

D^-_k(c,c')
 = [c'_0!/(c_d! prod_(i<d)e_i!)] C(k-r+c_d,c_d).      (2.2)
```

Moreover, fix rank-`r` owners `T,T'` at Johnson distance

```text
t=|T-T'|=|T'-T|.
```

There is a compatible labelled pair with owners `(T,T')` iff

```text
0<=t<=c_d.                                            (2.3)
```

When (2.3) holds, the exact number of compatible pairs is

```text
K_t(c,c')
 =(r-t)!/
   [(c_d-t)! prod_(i<d)c'_(i+1)! prod_(i<d)e_i!].      (2.4)
```

Thus the owner projection of one type edge is precisely the union of the
Johnson distance layers `0,...,c_d`, with the positive multiplicities
(2.4).

### Proof

For a fixed source, choose survivor cells

```text
S_i=C'_(i+1) subset C_i,       |S_i|=c'_(i+1).
```

The forced refreshed remainders have total size

```text
sum_(i<d)e_i=c'_0-c_d.
```

The remaining `c_d` members of `C'_0` can be chosen arbitrarily from
`C_d union ([k]-o(P))`, a set of size `k-r+c_d`.  This proves (2.1).
Reversing the construction, partition `c'_0-c_d` elements of `C'_0`
into ordered remainder cells of sizes `e_i`, then choose the old terminal
cell from a set of size `k-r+c_d`; this proves (2.2).

For fixed owners, put `I=T intersect T'`.  Any lost owner coordinate lies
in `C_d`, so `t<=c_d` is necessary.  Conversely, when `t<=c_d`, partition
`I` into the ordered cells

```text
S_i                 of size c'_(i+1),
R_i                 of size e_i,
K                   of size c_d-t.
```

Their sizes sum to `r-t`.  Then set

```text
C_i=S_i dotunion R_i                  (i<d),
C_d=(T-T') dotunion K,
C'_0=(T'-T) dotunion K dotunion_i R_i,
C'_(i+1)=S_i.
```

This is a bijection between compatible pairs and the displayed ordered
partitions of `I`, giving (2.4).  QED.

## 3. The exact owner-factor Hall cuts

Let `V` be any finite union of labelled age-state layers and let `D` be
the literal compatibility digraph on `V`.  A binary vector `x in {0,1}^V`
is an owner transversal when

```text
sum_(P:o(P)=T) x_P=1                 for every T in C([k],r).        (3.1)
```

Additional linear rows may prescribe the number of selected states of
each type.  Once `x` is fixed, there is a literal successor permutation on
the selected states iff

```text
x(A)<=x(N_D^+(A))                    for every A subseteq V.         (3.2)
```

Indeed, (3.2) is exactly Hall's theorem in the bipartite copy of the
induced digraph `D[supp x]`.  Its perfect matching is a successor
permutation, and every permutation component is a literal cyclic word by
(1.1).  Conversely every successor permutation certifies (3.2).

Before (3.2), owner naming alone has no obstruction.  If `U_c` is a set
of `A_c` abstract roles of type `c`, join every role in `U_c` to every
state in `Omega_c(k)`, and give the owner fibres capacity one.  Every role
sees every one of the `W=C(k,r)` owner fibres, so the Rado/Hall cuts reduce
to

```text
|S|<=W                              (S subseteq union_c U_c),        (3.3)
```

and hold because the total role count is `W`.  Hence symmetric owner
availability closes only the uncoupled owner SDR.  The nontrivial one-copy
condition is the induced-factor cut (3.2), followed by the nested named-
target rows.

If a role is already assigned a named prefix flag `F`, then its accessible
owner fibres are exactly `{T:F subseteq T}`.  For a frozen assignment of
flags to roles the exact owner SDR cuts become

```text
|S| <= |union_(u in S){T:F_u subseteq T}|             for all S.    (3.4)
```

Choosing the nested flags and the successor simultaneously is not an
ordinary consequence of (3.3); it is the remaining NRFC correlation.

## 4. Temporal girth

### Lemma 4.1 (age-`d` girth)

Every directed literal cycle containing a state with `C_d nonempty` has
length at least `d+1`.

### Proof

Let the emitted source cells on a cycle of length `L` be `B_t=C_(t,0)`,
with indices modulo `L`.  Iterating (1.1) gives

```text
C_(t,d)=B_(t-d) - union_(j=0)^(d-1) B_(t-j).          (4.1)
```

If `L<=d`, the `d` residues `t-d+1,...,t` modulo `L` include the residue
`t-d`.  Hence the right side of (4.1) is empty, a contradiction.  QED.

Consequently, if every selected type has positive terminal age, the
literal compatibility digraph induced by fewer than `d+1` selected states
is acyclic.  It has a sink, giving a singleton violated Hall cut in (3.2).

There is a stronger one-copy owner cut.  When a literal component has
length exactly `d+1`, every depth-`d` owner window is the union of the same
cyclic list of `d+1` source letters.  All its owners are therefore equal.
Consequently an owner-simple component containing a non-full source has
length at least `d+2`.

## 5. Sharp primitive-buffer theorem

Assume `d>=2` and `r>=d+2`, and put `h=r-d`.  Define

```text
H=(h,1,1,...,1),
P=(h-1,2,1,...,1).                                  (5.1)
```

These are precisely the two age types of the adjacent mixed rotor

```text
g_(d-1,d+1)=e_(d-1)+e_(d+1).                         (5.2)
```

### Theorem 5.1 (sharp minimum unmarked linear buffer)

A literal cycle whose type multiset consists of one `P` occurrence and
`n` occurrences of `H` requires

```text
n>=d                                                    (5.3)
```

and such a cycle exists at the sharp boundary `n=d`.  In particular, the
minimum possible `n` is `d`: the primitive rotor already contains one `H`,
so its smallest unmarked literal age-cycle repair uses exactly `d-1`
additional `H` buffer occurrences.  This statement does not assign the
rotor's marked target flags, and no assertion for every individual `n>d`
is needed here.

### Proof

The total length is `n+1`, and every state has terminal age one.  Lemma 4.1
gives `n+1>=d+1`, proving necessity.

For sufficiency at `n=d`, take a fixed owner

```text
T=K dotunion {q,e_0,...,e_d},        |K|=h-2,
```

and cyclic source cells, for `t in Z/(d+1)`,

```text
B_t=K union {e_t} union ({q} if t!=0).                (5.4)
```

The coordinate `e_(t-i)` has age `i` at time `t`.  The coordinate `q` is
of age one only at `t=0` and is fresh at every other time.  The coordinates
of `K` are always fresh.  Hence the age type at `t=0` is `P`, while every
other age type is `H`.  Every owner is the same set `T`, and (5.4) is a
literal period-`d+1` word.  QED.

### Corollary 5.2 (two buffers do not give a uniform local conversion)

Add at most two arbitrary positive-terminal buffer occurrences to one
primitive package (5.2).  The resulting inventory has at most four states.
For every `d>=4` it has no literal cycle factor, independently of `k`, the
choice of named owners, or target marks.  More generally, `m` primitive
packages plus `B` additional positive-terminal occurrences cannot be
locally physicalized whenever

```text
2m+B<d+1.                                             (5.5)
```

Thus no absolute bounded-multiplicity/bounded-buffer conversion theorem
can hold uniformly in `d`.  The first obstruction is temporal girth, not a
scarcity of owner labels.

For the actual owner-simple NRFC problem the stronger threshold is
`2m+B>=d+2`.  It is sharp for one primitive package: the independently
audited facet construction in
`MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`
uses the primitive pair plus exactly `d` low-buffer occurrences, on the
`d+2` distinct rank-`r` facets of one `(r+1)`-set, and has an injective
rankwise marked-prefix deck.

## 6. Exact consequence for NRFC

The large canonical buffer coordinates can still defeat this obstruction
globally: their stock is much larger than `d`, and NRFC permits rethreading
different formal packages into long cycles.  Therefore Corollary 5.2 is
not a counterexample to the canonical Ferrers NRFC assertion.

It does show that the weakest viable conversion theorem must be a **global
long-cycle pooling theorem**.  It must jointly select an owner transversal
`x` satisfying (3.1), the factor cuts (3.2), and the nested named-target
rows; no proof that physicalizes each aggregate rotor with `O(1)` private
buffers can be dimension-uniform.  After that one-copy factor is obtained,
Ore--Ryser completion, residence, upper/deep shadows, and common-cap
compatibility remain separate.
