# The exact even-dimensional equivariant `(c,t)` normal form

## 0. Statement and scope

Let `K=2r` be even, put `n=K-1=2r-1`, and distinguish the top coordinate
`z`.  Let

\[
 W=\binom{K}{r},\qquad N=\frac{W}{n}=2\operatorname{Cat}_{r-1}.
\]

Rotation `rho` acts cyclically on the `n` old coordinates and fixes `z`.
This note gives an exact normal form for a **rho-equivariant** cyclic
ordering of the rank-`r` layer with unit voltage.  It does not assert that
every optimum is equivariant: the retained `k=10,12` optima are not, and
the retained `k=14` optimum is only partly equivariant.  The value of the
normal form is that it turns the first open case `k=16` into a compact
construction problem rather than a 12,870-vertex free routing problem.

## 1. Reconstruction from two binary words

Let

\[
 c\in\{0,1\}^{W},\qquad t\in\{0,1\}^{N}
\]

be cyclic words.  Extend `t` periodically to physical indices.  Define

\[
 T_i=\bigl(\{z\}:t_{i\bmod N}=1\bigr)
      \cup
      \{x\in\mathbb Z_n:c_{i-xN}=1\},
 \qquad i\in\mathbb Z_W.
\tag{1.1}
\]

Then automatically

\[
 T_{i+N}=\rho(T_i).
\tag{1.2}
\]

Conversely, every unit-voltage equivariant chronology has the form (1.1):
take `c_i=1_{0 in T_i}` and `t_j=1_{z in T_j}`.  A coprime nonunit voltage
is removed by multiplying the old coordinate labels by its inverse modulo
`n`, so unit voltage loses no generality **for this single quotient
component/global cyclic chronology**, provided the admitted construction
class is closed under that coordinate multiplier.  It is not a WLOG
reduction for several quotient components: only one common multiplier is
available, and their relative voltages survive.  The exact multi-component
scope is given in
`MATH_THEOREM_AD_EVEN_MULTICOMPONENT_CT_WAKSMAN_NORMAL_FORM_20260729.md`.

## 2. Rank and Johnson laws

For a residue class `j in Z_N`, define

\[
 C_j=\{a\in\mathbb Z_W:a\equiv j\pmod N,\ c_a=1\}.
\]

### Theorem 2.1 (class-sum law)

Every `T_i` has rank `r` if and only if

\[
 |C_j|=r-t_j\qquad(j\in\mathbb Z_N).
\tag{2.1}
\]

### Proof

As `x` ranges over `Z_n`, the indices `i-xN` are exactly the `n` positions
of the residue class `i mod N`.  Hence the old-coordinate rank of `T_i` is
`|C_{i mod N}|`, and `z` contributes `t_i`.  `square`

For transition class `j`, let

\[
 s_j=\#\{a\equiv j\pmod N:(c_a,c_{a+1})=(0,1)\},
\]

\[
 e_j=\#\{a\equiv j\pmod N:(c_a,c_{a+1})=(1,0)\}.
\]

These are respectively the numbers of old coordinates inserted and
deleted at every physical transition in quotient class `j`.

### Theorem 2.2 (even transversality law)

Under (2.1), consecutive states are distinct Johnson neighbours exactly
when

\[
 (s_j,e_j)=
 \begin{cases}
 (1,1),&t_j=t_{j+1},\\
 (0,1),&(t_j,t_{j+1})=(0,1),\\
 (1,0),&(t_j,t_{j+1})=(1,0).
 \end{cases}
\tag{2.2}
\]

Equivalently, `c` has one run-start in every quotient class except a
class where `t` starts a 1-run, and one run-end in every class except a
class where `t` ends a 1-run.

### Proof

The old symmetric difference has size `s_j+e_j`; the top contributes
`|t_{j+1}-t_j|`.  Equality of the two ranks gives

\[
 s_j-e_j=t_j-t_{j+1}.
\]

A distinct Johnson step has total symmetric difference two.  Solving these
two equations in the three possible top-transition cases gives (2.2), and
the converse is immediate.  `square`

If `t` has `h` cyclic 1-runs, then `c` has exactly `N-h` runs.  At `k=16`,
this is `858-h` runs rather than one run per quotient class.

## 3. Hamilton/layer condition

For each quotient class define its old-coordinate column

\[
 S_j=\{x\in\mathbb Z_n:c_{j-xN}=1\}.
\tag{3.1}
\]

Rotation on the rank-`r` and rank-`(r-1)` layers of `[n]` is free.  Indeed,
a nontrivial stabilizer partitions `Z_n` into equal orbits whose length
would divide `r` or `r-1`, impossible because

\[
 \gcd(2r-1,r)=\gcd(2r-1,r-1)=1.
\]

Each layer therefore has

\[
 \frac1n\binom nr=\frac1n\binom n{r-1}
   =\operatorname{Cat}_{r-1}=N/2
\]

necklace orbits.

### Theorem 3.1 (two simultaneous zero-spare bijections)

The states (1.1) enumerate the complete rank-`r` layer of `[K]` exactly
once if and only if

1. `t` has exactly `N/2` zeros and `N/2` ones;
2. the columns `S_j` with `t_j=0` represent every rotation orbit of
   rank-`r` old subsets exactly once;
3. the columns `S_j` with `t_j=1` represent every rotation orbit of
   rank-`(r-1)` old subsets exactly once.

Thus the middle-layer condition has no slack in either sector.

## 4. Residence

Every old coordinate trace is a cyclic shift of `c`; the top trace is `t`
repeated `n` times.  Consequently depth-`d` residence is equivalent to

\[
 \min\{\text{cyclic 1-run lengths of }c\}\ge d+1,
 \qquad
 \min\{\text{cyclic 1-run lengths of }t\}\ge d+1.
\tag{4.1}
\]

At `k=16`, `r=8`, `W=12870`, `N=858`, `d=3`; hence `t` is an
`858`-bit cyclic word with exactly `429` ones, all in runs of length at
least four.  The class sums of `c` are `8-t_j`.

## 5. Exact q1 accounting

Let `h` be the number of cyclic 1-runs of `t`.  Among the `N` quotient
transitions there are

\[
 \#AA=N/2-h,quad \#BB=N/2-h,quad \#AB=\#BA=h.
\tag{5.1}
\]

After physical lifting by `n`, q1 intersections not containing `z` are
supplied by AA, AB, and BA edges, while q1 intersections containing `z`
are supplied only by BB edges.  At `k=16` this gives

\[
 \begin{aligned}
 \text{no-}z\text{ occurrences}&=15(429+h),\\
 z\text{-occurrences}&=15(429-h).
 \end{aligned}
\tag{5.2}
\]

The target counts are `C(15,7)=6435` and `C(15,6)=5005`.  The raw
physical count therefore gives

\[
 15(429-h)\ge5005,qquad\text{hence }h\le95.
\tag{5.3}
\]

There is a sharper quotient count.  Rotation on the old rank-`6` layer
has `335` necklace orbits: `333` have size `15`, while `2` have size `5`.
Indeed Burnside gives

\[
 \frac{1}{15}\left(\binom{15}{6}+2\binom52\right)=335.
\]

Each BB quotient edge can cover only one such orbit, so exact lower-q1
coverage actually forces

\[
 429-h\ge335,\qquad\boxed{h\le94}.
\tag{5.4}
\]

The same bound follows independently on the upper-q1 side: only the
`429-h` AA quotient edges can realize a no-top rank-`9` union, and
complementation identifies its necklace classes with the same `335`
rank-`6` classes.  Thus `h<=94` is a genuine two-sided orbit-capacity
constraint, not an artifact of counting physical occurrences.

The total q1 surplus is the forced

\[
 12870-\binom{16}{7}=1430.
\]

Unlike odd `k`, q1 is not a bijection, but the complete even answers at
`k=10,12,14` all attain zero q1 holes.  The exact `k=16` search should
therefore impose zero holes, not rely on the two compiler boundary slots.

## 6. What remains to construct

The equivariant `k=16` problem is now:

1. choose `t` as above, with at most `94` runs;
2. choose `c` satisfying (2.1), (2.2), and (4.1);
3. enforce the two necklace bijections of Theorem 3.1;
4. enforce zero q1 holes and arbitrary-width upper completeness;
5. reconstruct the physical chronology, solve exact `COMP_3` with an
   actual required source mask `{z}`, and exhaustively verify the resulting
   `12873`-letter word.

This is an exact sufficient construction route.  Existence for all even
`k`, or even for `k=16`, remains open.  Its main advantage over the free
rail/rung master is compression: the sector schedule is only `858` bits,
and the middle Hamilton constraint is two explicit orbit permutations.
