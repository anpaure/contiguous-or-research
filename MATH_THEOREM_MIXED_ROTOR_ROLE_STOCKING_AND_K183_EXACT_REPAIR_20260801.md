# Mixed-rotor role stocking and an exact repair of the `k=183` residual row

Date: 2026-08-01  
Lane: integral age-level sequel to the monotone-rotor fractional theorem  
Status: unconditional role-stocking criterion and explicit `k=183` repair.
This closes the first nonfull self-loop obstruction at the invariant integral
marked-age level.  It does not produce one-copy owners or a physical
contiguous-OR chronology.

## 1. Why a full positive rotation is the wrong packet

For odd `k=2r-1`, the triangular demand at deficit one is

```text
n_1=C(k,r-1)=W.                                       (1.1)
```

Thus every one of the `W` age rows must offer deficit `1`, equivalently its
oldest age class must have size one.

Let `c=(c_0,...,c_d)` be a positive composition with `r>d+1`.  Some
component is larger than one.  Its full cyclic coordinate-rotation orbit
places that component in coordinate `d` in one phase, and that phase does
not offer deficit one.  Therefore:

### Proposition 1.1 (odd full-rotation stock obstruction)

No nontrivial full positive-coordinate rotation orbit can occur with
positive multiplicity in an exact odd-dimensional marked law satisfying
(1.1).

This is the occurrence-stock form of the known fractional inequality
`a_(r-1)=a_1<=d/(d+1)`.  It explains exactly why the locally valid ten-state
rotation completion of the `k=183` row cannot be stocked globally.

## 2. The mixed prefix rotor

Let `F={f_1<...<f_d}` be a full deficit profile and let

```text
c(F)=(r-f_d, f_d-f_(d-1), ..., f_2-f_1, f_1).        (2.1)
```

Assume `[a] subseteq F` for some `1<=a<d`.  Then the last `a` age classes
in (2.1) are singletons.  Put `D=d-a` and write

```text
c=(x_0,x_1,...,x_D,1,...,1),                         (2.2)
```

with `a` terminal ones.  Define

```text
tau(c)=(x_D,x_0,x_1,...,x_(D-1),1,...,1).            (2.3)
```

### Theorem 2.1 (mixed-prefix rotor cycle)

The orbit

```text
c -> tau(c) -> ... -> tau^D(c) -> c                 (2.4)
```

is a legal stationary age cycle of length dividing `D+1`.  Every phase
offers all deficits `1,...,a`.

#### Proof

For indices `i<D`, the transition inequality is equality:

```text
(tau c)_(i+1)=c_i.
```

At the interface `i=D`, the target begins the frozen singleton rail, so

```text
(tau c)_(D+1)=1<=c_D.
```

Every later comparison is `1<=1`.  Rotation of the prefix returns after
`D+1` steps, proving stationarity.  The frozen terminal rail has cumulative
suffix sums `1,...,a` in every phase.  QED.

This is the integral one-orbit version of the mixed rotor in the new
monotone-rotor theorem.  Its essential feature is not merely a shorter
period: it preserves the saturated deficit-one column phase by phase.

### Corollary 2.2 (every nonfull profile has a mixed-rotor completion)

Assume `r-1>=d`.  Let `A` be any marked profile with `|A|<d`.  Extend it to
a `d`-set `F subseteq [r-1]` which contains deficit `1`, and let

```text
a=max{j:[j] subseteq F}>=1.
```

Then Theorem 2.1 gives a stationary mixed-rotor cycle of at most `d` roles
whose distinguished phase supports `A` and every one of whose phases
supports deficit `1`.

#### Proof

There is at least one spare mark, so deficit `1` can be added if necessary;
the remaining spare marks can be chosen arbitrarily.  Formula (2.1) then has
`a` terminal singleton classes.  Its prefix period is
`d-a+1<=d`.  QED.

Thus the `k=183` phenomenon is not a failure of local stationary age
completion.  It is the first failure of the much narrower self-loop
completion.  The true issue is simultaneous role stock, handled next.

## 3. Exact fixed-role stocking criterion

Let the global marked demands be `n_t` on `W` named rows of capacity `d`.
Reserve role categories `j=1,...,J`.  Category `j` has:

* multiplicity `b_j`;
* available deficit set `D_j`, with `|D_j|<=d`; and
* a forced marked subset `F_j subseteq D_j` on every copy.

Put

```text
M=sum_j b_j,
U=W-M,
N=sum_t n_t.                                         (3.1)
```

### Theorem 3.1 (integral role-bank extension)

The reserved bank extends to an exact marked assignment on all `W` rows if
and only if there are integers `x_(t,j)` satisfying

```text
b_j 1[t in F_j] <= x_(t,j) <= b_j 1[t in D_j],

(n_t-U)_+ <= sum_j x_(t,j) <= n_t,                  (3.2)

sum_t x_(t,j) <= d b_j,

sum_(t,j) x_(t,j) >= (N-dU)_+.                       (3.3)
```

This is an exact integral lower-bound flow problem.  Hence feasibility is
decidable by one max-flow/min-cut computation, and every failure has an
integral cut certificate.

#### Proof

Necessity is immediate.  Let `g_t=sum_j x_(t,j)`.  The `U` unreserved rows
must carry `n_t-g_t` copies of mark `t`, giving the lower and upper column
bounds in (3.2), while their total capacity gives (3.3).

Conversely, for each role category, the inequalities

```text
x_(t,j)<=b_j,
sum_t x_(t,j)<=d b_j
```

are exactly the complete-bipartite degree criterion for assigning those
marks to `b_j` distinct copies with row capacity `d`.  After doing so, the
residual degrees obey

```text
0<=n_t-g_t<=U,
sum_t(n_t-g_t)<=dU.
```

The complete-bipartite stocking theorem therefore assigns them to the `U`
free rows.  All matrices are bipartite network matrices, so the construction
is integral.  QED.

One explicit lower-bound network has arcs

```text
source -> deficit t       [(n_t-U)_+, n_t],
deficit t -> role j       [b_j 1[t in F_j], b_j 1[t in D_j]],
role j -> sink            [0,d b_j],
sink -> source            [(N-dU)_+, dM].             (3.4)
```

Thus Theorem 3.1 is also the requested exact Hall/Strassen min-cut form for
a fixed stationary packet bank.

### Corollary 3.2 (simple singleton-rail stock test)

Suppose every one of `M` reserved mixed-rotor roles supports deficit `1`,
and the distinguished anchors carry `E` additional marks in total.  Mark
only deficit `1` on every role and those `E` anchor marks.  If

```text
W-n_2>=M,
dW-N >= (d-1)M-E,                                    (3.5)
```

then the bank extends.

Indeed, `g_1=M`, so the saturated first column leaves exactly `U=W-M`
copies.  For `t>=2`, monotonicity gives `n_t-g_t<=n_2<=U`.  The second
inequality in (3.5) is precisely

```text
N-(M+E)<=d(W-M).
```

Theorem 3.1 completes the assignment.

## 4. Exact `k=183` mixed-rotor repair

At

```text
k=183, r=92, d=9,
```

the first nonfull systematic profile without a self-loop completion is

```text
A={1,2,4,5,6,8,9,13},                                (4.1)
```

of multiplicity

```text
mu=285916660092460398796273644655925707923024842785460.
                                                               (4.2)
```

Complete it by the unmarked deficit `3`:

```text
F=A union {3},
c(F)=(79,4,1,2,1,1,1,1,1,1).                        (4.3)
```

Freeze the last three singleton classes and rotate the seven-entry prefix.
Theorem 2.1 gives a seven-role stationary cycle, and every role offers
deficits `1,2,3`.

Take `mu` copies of this cycle.  Mark every one of its seven roles at
deficit `1`; on the distinguished phase also mark the other seven members
of `A`.  Thus

```text
M=7mu,
g_1=7mu,
g_t=mu for t in A\{1},
g_t=0 otherwise.                                      (4.4)
```

All marked subsets are available: the anchor has profile `F`, and the
singleton rail supplies mark one everywhere.

For the canonical triangular boundary, the exact inequalities are

```text
W-n_2
=15487357822491889407128326963778343232013931127835600
>7mu
= 2001416620647222791573915512591479955461173899498220,
                                                               (4.5)

9W-N
=351477085249300283449816725739999908122873688264789897
>49mu
= 14009916344530559541017408588140359688228217296487540.
                                                               (4.6)
```

Since `n_1=W`, equation (4.4) gives `n_1-g_1=W-M=U` exactly.  For every
`t>=2`, monotonicity and (4.5) give

```text
n_t-g_t<=n_2<=U.                                      (4.7)
```

The bank uses `14mu` marked slots: seven mark-one slots plus seven extra
anchor marks.  Equation (4.6) is exactly

```text
N-14mu <= 9(W-7mu)=dU.                                (4.8)
```

Therefore all inequalities of Theorem 3.1 hold.

### Corollary 4.2

The `k=183` nonselfloop row has an exact stationary, rank-neutral mixed-rotor
repair inside the original `W` age rows.  No extra age row and no literal
sidecar is needed at this quotient level.

This repair is genuinely mixed.  By Proposition 1.1, none of the possible
full positive-coordinate rotation completions can stock at odd `k=183`.

## 5. The first single-packet global obstruction is `k=220`

The mixed rotor repairs the first nonfull self-loop failure, but independent
per-profile packetization is not a general theorem.

At

```text
k=220, r=110, d=9,
```

the canonical systematic law has one nonfull nonselfloop profile

```text
A={1,2,4,5,6,8,9,12}                                 (5.1)
```

of multiplicity

```text
mu=3633781894179592609405814541720303407075174209554631661639214480.
                                                               (5.2)
```

Every mixed-prefix completion adds one mark `x notin A`.  For any proposed
role bank let `C_t` be the number of reserved roles supporting deficit `t`,
counted with multiplicity.  Regardless of row-level assignment, the bank can
receive at most

```text
sum_t min(n_t,C_t)                                      (5.3)
```

marks.  On the other hand, removing `M` roles forces it to receive at least

```text
N-d(W-M)                                                (5.4)
```

marks, or the free rows lack total capacity.

The exact exhaustive completion audit proves (5.3)<(5.4) for every possible
added mark.  The best case is `x=3`, with completion

```text
F={1,2,3,4,5,6,8,9,12}.                                (5.5)
```

It freezes a six-singleton rail and rotates four prefix blocks.  Even there,

```text
required bank marks
=113196835487925761106174329535650594158084844237762191236419883727,

maximum available marks
=109013456825387778282174436251609102212255226286638949996281774705,

deficit
=  4183378662537982823999893284041491945829617951123241240138109022.
                                                               (5.6)
```

Thus no **single** mixed-rotation completion of (5.1) can be stocked, even
though each is a valid local stationary cycle.

This is not a Strassen obstruction to the global monotone-rotor theorem.
It says that cycles must be selected from the aggregate demand, sharing
roles across marked profiles; one cannot repair every bad row independently.
The H100 O3 scan checks all canonical-boundary instances through `k=300`:
the lexicographic mixed-packet scheme passes through `k=219` and first fails
at (5.1), while the all-completion census makes the `k=220` failure robust.

## 6. Relation to `k=140`

The noncanonical full extreme row

```text
{1,2,4,5,7,9,69}
```

at `k=140` is already repaired by the arbitrary-hole parity actuator and
the arbitrary-extreme stocking theorem.  It also has a two-singleton mixed
prefix rotor, but that stronger packet is unnecessary.  Thus the two first
classification failures are now both closed at the marked-age level:

```text
k=140: arbitrary-hole parity packet;
k=183: frozen-singleton mixed rotor.
```

## 7. Remaining scope

The result proves a stationary **age-type** packet and exact global marked
degree extension.  It still does not prove:

* one occurrence-labelled owner per rotor role;
* owner-changing Johnson transitions with exact q1 palettes;
* fusion of the rotor cycles into one rooted chronology;
* arbitrary-width upper protection or common-cap matching.

The monotone-rotor theorem closes the invariant fractional cone for every
`k`; Theorem 3.1 is the exact integral interface for stocking any proposed
finite rotor bank.  The `k=220` cut shows that the next age-level theorem is
an aggregate integral decomposition into mixed rotors, followed by coloured
owner fusion—not another Strassen inequality and not independent local
completion.

## 8. Audit artifacts

```text
scratch/audit_global_rotation_role_packing_20260801.cpp
SHA256 01a9571fcdbde2e20e0c68d5373aac361a8b2740c039dc051d9c857d283120b6

scratch/global_rotation_role_packing_20260801.audit.json
SHA256 ae98c74720a1d915e4a04e34a96dbca57378ff7943da19e59935ac084245f5e3
status PASS_GLOBAL_ROTATION_ROLE_PACKING_AUDIT
```

The final version of the checker was compiled with `g++ -O3 -DNDEBUG` and
run on one H100-host CPU core.  It uses exact arbitrary-precision arithmetic,
exact breakpoint histograms, exact self-loop dynamic programming, integral
Dinic flow for both literal-profile Hall and the lower-bound marked-role
network, and the scalar total-cut replay (5.3)--(5.6).
