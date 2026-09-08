# Monotone rotors close the invariant fractional trace gate

Date: 2026-08-01

Status: unconditional fractional theorem, independently audited.  Every
monotone rank-demand vector of total mass at most the trace depth has a
literal same-owner labelled trace circulation.  Applied to a left-filled
optimal Ferrers boundary, this closes the invariant fractional triangular
trace gate for every `k>=3`.  It does **not** give one trace per owner, an
integral owner/target SDR, owner-changing rotor fusion, connected/rooted
support, source-letter residence, upper shadows, or a common cap.

## 1. Literal invariant trace projection

Fix integers

```text
k>=r>d>=1.                                             (1.1)
```

An age type is

```text
c=(c_0,...,c_d),       c_0>0, c_i>=0, sum_i c_i=r.   (1.2)
```

Its proper prefix/suffix-cell ranks are

```text
s_j(c)=c_0+...+c_(j-1),       1<=j<=d.               (1.3)
```

Repeated values in (1.3) are one target colour, not multiple rank capacity.
All types used in the rotor constructions below are positive, so their
displayed ranks are distinct.

For a fixed owner `T in binom([k],r)`, a labelled state of type `c` is an
ordered partition

```text
T=C_0 dotunion ... dotunion C_d,       |C_i|=c_i.    (1.4)
```

A particular state `C` of type `c` may precede a particular state `C'` of
type `c'` precisely when

```text
C'_(i+1) subseteq C_i       (0<=i<d),                (1.5)
```

A compatible labelled pair of these two types exists if and only if

```text
c'_(i+1)<=c_i       (0<=i<d).                        (1.6)
```

The emitted nonempty source letter is `C'_0`.  A directed cycle of states
satisfying (1.5) spells a literal periodic word by taking its successive
age-zero classes; every consecutive `(d+1)`-window has owner `T`.

Let `ST_(k,r,d)` be the rank-mark projection of normalized nonnegative
circulations on these literal states, averaged over all rank-`r` owners and
coordinate permutations.  Marks may be assigned only to distinct ranks
offered by (1.3).  Thus `q_s` is the marked mass of rank `s` per owner, not
an integral target assignment.

Define

```text
M_(r,d)={q in R^(r-1):
          0<=q_1<=...<=q_(r-1)<=1,
          sum_(s=1)^(r-1) q_s<=d}.                   (1.7)
```

### Theorem 1.1 (monotone rotor theorem)

For every range (1.1),

```text
                         M_(r,d) subseteq ST_(k,r,d). (1.8)
```

## 2. Exact labelled biregular lift

The passage from age types to literal states is lossless fractionally.

### Lemma 2.1 (labelled lift)

Let `f_(c,c')>=0` be a normalized circulation on legal type edges:

```text
sum_c' f_(c,c')=sum_c' f_(c',c)=pi_c,
sum_c pi_c=1.                                         (2.1)
```

Then `f` has a literal labelled-state lift on every fixed owner `T`, uniform
on all states of each type.  A type-dependent marking of offered ranks lifts
with the same rank marginals.

### Proof

The number of states of type `c` is

```text
N_c=r!/prod_(i=0)^d c_i!.                             (2.2)
```

For a legal edge `c->c'`, the compatibility graph (1.5) has fixed source
degree

```text
D^+_(c,c')=prod_(i=0)^(d-1) binom(c_i,c'_(i+1)),     (2.3)
```

because the survivor class `C'_(i+1)` is chosen independently inside
`C_i`.  Its fixed target degree is

```text
D^-_(c,c')
 =c'_0!/[c_d! prod_(i=0)^(d-1)(c_i-c'_(i+1))!],     (2.4)
```

because `C'_0` is partitioned into the old terminal class of size `c_d`
and the refreshed remainders of sizes `c_i-c'_(i+1)`.  Hence

```text
E_(c,c')=N_c D^+_(c,c')=N_c' D^-_(c,c').            (2.5)
```

Put weight `f_(c,c')/E_(c,c')` on every compatible labelled arc.  Each
source state receives outgoing mass `f_(c,c')/N_c` from this type edge, and
each target state receives incoming mass `f_(c,c')/N_c'`.  Summing and using
(2.1) gives both incoming and outgoing mass `pi_c/N_c` at every state of
type `c`.  This is a literal circulation by (1.5), and uniformity makes every
offered target of a fixed rank uniform.  QED.

For rational `f` and rational mark splits, clearing their common denominator
and decomposing the labelled Eulerian multigraph gives an integral marked
**multicover**.  It generally repeats owners and targets.  Lemma 2.1 is not
a one-copy chronology theorem.

## 3. Vertices of the monotone polytope

For `1<=ell<=r-1`, let `v_ell` be the vector which is one on ranks

```text
r-ell,...,r-1
```

and zero below.  Every nondecreasing `q` has the unique representation

```text
q=sum_(ell=1)^(r-1) alpha_ell v_ell,
alpha_ell>=0,
sum_ell alpha_ell<=1,
sum_ell ell alpha_ell<=d.                             (3.1)
```

Indeed the `alpha` values are the successive increments of `q`, read from
the top, and the last two left sides in (3.1) equal `q_(r-1)` and
`sum_s q_s`, respectively.

### Lemma 3.1 (complete vertex list)

The vertices of (3.1) are

```text
0;
v_a                                                     (1<=a<=d);
(d/b)v_b                                                (d<b<=r-1);
((b-d)/(b-a))v_a+((d-a)/(b-a))v_b
                                           (1<=a<d<b<=r-1). (3.2)
```

### Proof

Besides nonnegativity, (3.1) has only two scalar inequalities, so a vertex
has at most two positive `alpha` coordinates.  A one-coordinate vertex
makes either `sum alpha=1` (index at most `d`) or
`sum ell alpha=d` (index above `d`), giving the first two nonzero families.
A two-coordinate vertex makes both inequalities tight.  Its indices must
straddle `d`, and solving the two equations gives the final coefficients.
QED.

## 4. Explicit clocks for every vertex

### 4.1 Short suffixes

Put

```text
H=(r-d,1,...,1).                                      (4.1)
```

It has a legal self-loop and offers all ranks `r-d,...,r-1`.  Marking only
its top `a` offered ranks realizes `v_a`, for `1<=a<=d`; marking none
realizes zero.

### 4.2 Long rotor

Fix `d<b<=r-1`.  Let

```text
A_(b,d)={a=(a_0,...,a_d) in Z_>0^(d+1):sum_i a_i=b+1}.
```

For `a in A_(b,d)`, use type

```text
c(a)=(r-b-1+a_0,a_1,...,a_d),                        (4.2)
```

and the cyclic block rotation

```text
rho(a)=(a_d,a_0,...,a_(d-1)).                        (4.3)
```

The edge `c(a)->c(rho(a))` is legal: coordinates `2,...,d` are equalities,
and coordinate one uses `a_0<=r-b-1+a_0`.  Uniform mass on these edges is a
type circulation because `rho` permutes `A_(b,d)`.

Positive compositions of `b+1` into `d+1` parts are in bijection with
`d`-subsets of the `b` cut positions.  The ranks (1.3) are the cut positions
shifted by `r-b-1`.  Hence every rank in `r-b,...,r-1` is offered with
probability exactly `d/b`.  Marking every offered rank realizes

```text
                              (d/b)v_b.               (4.4)
```

### 4.3 Mixed rotor

Fix `1<=a<d<b<=r-1` and put

```text
D=d-a,       L=b-a,       R=r-a.                    (4.5)
```

Run the long rotor of Section 4.2 with owner rank `R`, depth `D`, and long
length `L`, then append `a` terminal singleton age classes to every type.
The interface inequality is `1<=x_D`, where `x_D` is the positive final
mobile block; the later inequalities are `1<=1`.  Thus the extended rotor is
legal.

Its reduced part offers ranks `r-b,...,r-a-1` with probability

```text
D/L=(d-a)/(b-a),
```

while the appended rail offers every rank `r-a,...,r-1` with probability
one.  Its marked vector is therefore

```text
((b-d)/(b-a))v_a+((d-a)/(b-a))v_b.                  (4.6)
```

Sections 4.1--4.3 realize every vertex in Lemma 3.1.  Convex combinations,
followed by Lemma 2.1, prove Theorem 1.1.

## 5. Optimal Ferrers boundary

Now fix `k>=3` and put

```text
r=ceil(k/2),
W=binom(k,r),
Lambda=sum_(s=1)^(r-1) binom(k,s),
d=min{q>=0:qW+binom(q+1,2)>=Lambda},
h=(Lambda-dW)_+.                                    (5.1)
```

Then

```text
1<=d<=r-1,       0<=h<=binom(d+1,2).
```

The first bound uses `Lambda<= (r-1)W`; the second is the defining
inequality for `d` when `h>0`.

On the triangular board

```text
F_d={(i,s):1<=s<=i<=d},                             (5.2)
```

select exactly `h` cells by filling columns `s=1,2,...` completely in that
order, with at most one partially filled final column.  Let `b_s` be the
number selected in column `s`, and define

```text
b_s=0              for d<s<r.                       (5.3)
```

Then

```text
b_1>=b_2>=...>=b_(r-1)>=0,
sum_s b_s=h.                                         (5.4)
```

### Corollary 5.1 (the triangular invariant fractional trace gate is closed)

The residual vector

```text
q_s=[binom(k,s)-b_s]/W,       1<=s<r,               (5.5)
```

belongs to `ST_(k,r,d)`.

### Proof

Every `b_s` is at most `d<=k<=binom(k,s)`, and
`binom(k,s)<=W` for `s<r`.  Thus `0<=q_s<=1`.  The binomial coefficients
increase through rank `r-1`, while (5.4) is nonincreasing, so

```text
q_(s+1)-q_s
 =[binom(k,s+1)-binom(k,s)+b_s-b_(s+1)]/W>=0.       (5.6)
```

Finally,

```text
sum_(s=1)^(r-1)q_s=(Lambda-h)/W<=d.                 (5.7)
```

Hence `q in M_(r,d)`, and Theorem 1.1 applies.  QED.

For a fixed rank-`s` target, the central same-owner load is

```text
binom(k-s,r-s) q_s/binom(r,s)
 =W q_s/binom(k,s)
 =1-b_s/binom(k,s),                                 (5.8)
```

exactly complementary to the load `b_s/binom(k,s)` supplied by the common
singleton-prefix Ferrers boundary.  Thus there is no invariant fractional
rank, trace-balance, or boundary-load obstruction.

## 6. The exact surviving integral gate

The theorem proves a convex combination of literal same-owner trace cycles.
It does not choose one trace for each of the `W` owners or one occurrence of
each target.  It also does not connect the cycles, move between owners,
preserve source-letter residence, cover upper shadows, or solve common-cap
and compiler constraints.

There is rigidity even before those guards.  On the core-free positive-
composition rotor, let `F` be a bijective successor map on
`A_(b,d)` satisfying (1.6).  Summing

```text
F(a)_(i+1)<=a_i
```

over all `a` gives equality because `F` is a permutation and the positive-
composition set is coordinate-symmetric.  Hence equality holds termwise,
so

```text
F(a)=(a_d,a_0,...,a_(d-1)).                         (6.1)
```

Thus a different one-successor matching on the same rotor states cannot
perform the integral fusion.  The next theorem must correlate different
owners/target occurrences or add a colour-carrying actuator.

This construction is an alternative unconditioned fractional realization
of the target vector.  It does not assert feasibility after prescribing the
specific donor/reservoir/actuator occurrences of another realization as
lower bounds.  If those rows are retained, a conditioned residual
circulation remains a separate gate.

For the new rotor route itself, the exact remaining physical problem is:

> round the invariant rotor mixture to one occurrence per owner and target,
> fuse its owner-labelled cycles, and satisfy the protected two-factor
> Ore--Ryser cuts together with residence, deep-shadow, and common-cap
> guards.

No `B(k)+O(1)` or exact all-`k` conclusion is asserted.
