# Audit of the monotone-radius rotor braid proposal

## Verdict

The variable-radius transition and the monotone-profile atom are valid, but
their proof needs a refined-state invariant.  After one MTF update the state
is generally **not** the canonical partition `Pi_(t+1)(e)`, even when `e=d`.
Old singleton blocks remain split off from the residual block.  They occur
strictly after all blocks needed by the next symmetric chain, and under a
nonincreasing radius profile they remain harmless forever.

The initialization count `H+2d_0+1` is exact, and every exposed chain member
is a literal suffix OR of the claimed word, not merely a formal prefix union.
The queue-size hypothesis is sufficient for pairwise distinct coordinates.

The fractional profile calculation is also correct.  For the invoked
**width-order tail construction**, the proposed range is too broad as
written: its proved uniform theorem needs `omega=o(m^(1/3))`, not merely
`omega=o(m)`.  Choosing `omega=log m` repairs this without affecting the
reset estimate.  This should not be confused with literal enumeration of
the outside masks, which has a larger tail ledger.  The integral packing
lemma remains an explicit unproved gate, and its statement must explicitly
retain the per-rank incidence quotas.

## 1. Queue feasibility

The inclusive queue range

```text
-h, -h+1, ..., H+m-1
```

has `H+m+h` indices.  Since `H<=m-h`, this is at most `2m`, so it can be
injected into the coordinate set.  The chains and transitions actually use
indices only through `H+m-2`; the final listed coordinate is harmless spare
queue capacity.  The minimum used index is `-h`.

For every `d<=h<m`, both end blocks of `Pi_t(d)` have size `m-d>=1`.
Consequently all initialization entries and all update masks are nonempty.

## 2. Exact local MTF transition

Let `R_t^(d)` denote the last block of the canonical partition.  For
`0<=e<=d`, put

```text
X = {z_(t+e+1), ..., z_(t+m)}.
```

Direct block subtraction gives the unified formula

```text
M_X(Pi_t(d)) =
  (X, {z_(t+e)}, {z_(t+e-1)}, ..., {z_(t-d)},
      R_t^(d) - {z_(t+m)}).
```

When `e<d`, the old `L_t^(d)` is wholly absorbed by `X`; the first surviving
old singleton is `{z_(t+e)}`.  When `e=d`, the residual

```text
L_t^(d) - X = {z_(t+d)}
```

is exactly the first singleton shown above.  Thus the proposal's special
`e=d` observation is correct.

The first `1+2e` blocks are

```text
X, {z_(t+e)}, ..., {z_(t+1)}, {z_t}, ..., {z_(t+1-e)},
```

which are precisely the chain blocks of `Pi_(t+1)(e)`.  Their prefix unions
are `C(t+1,e)`.

The complete updated state is not canonical: it additionally retains

```text
{z_(t-e)}, ..., {z_(t-d)}
```

as singleton blocks instead of merging them into the residual.  The smallest
legal transition exhibiting this is `m=3,h=1,H=2`; already `d=e=0` leaves
`{z_t}` as an extra singleton after the new radius-zero center.

## 3. Refined-state induction

Let `d_0>=...>=d_(H-1)` and write `U` for the complete coordinate set.  The
actual state after the chain at time `t` is exposed is

```text
PiHat_t = (
  L_t^(d_t),
  {z_(t+d_t-1)}, {z_(t+d_t-2)}, ..., {z_(-d_0)},
  RHat_t
),

RHat_t = U - {z_(-d_0), ..., z_(t+m-1)}.
```

This holds at `t=0`.  If `e=d_(t+1)<=d_t`, updating by

```text
L_(t+1)^e = {z_(t+e+1), ..., z_(t+m)}
```

produces

```text
(
  L_(t+1)^e,
  {z_(t+e)}, ..., {z_(-d_0)},
  RHat_t - {z_(t+m)}
),
```

which is exactly `PiHat_(t+1)`.  Since

```text
t-d_t >= -d_0,
```

the first `1+2d_t` blocks of `PiHat_t` are the canonical blocks exposing
`C(t,d_t)`.  All stale singletons occur later.  This proves the full
monotone-profile claim without assuming that MTF merges old blocks.

Different exposed masks cannot collide.  Masks at different depths have
different ranks.  At one fixed depth, changing `t` shifts a nonempty proper
interval in the injective coordinate queue, deleting one coordinate and
adding another.

## 4. Initialization and literal suffix ORs

The canonical initial partition has exactly `2d_0+2` nonempty blocks.  Write
these blocks in reverse order.  At the endpoint of this initialization, its
literal suffix unions are exactly the prefix unions of `Pi_0(d_0)`.

Appending each of the `H-1` later update masks applies the standard exact
last-occurrence identity

```text
Pi -> (X, B_1-X, ..., B_s-X),
```

with empty differences deleted.  Hence at every endpoint the state-prefix
unions are exactly literal suffix ORs of the word ending there.  The word
length is therefore

```text
(2d_0+2) + (H-1) = H+2d_0+1.
```

No factorability or coordinate-pin hypothesis is being smuggled into this
step: these are actual entries of an actual OR word.

## 5. Fractional profiles

The vector `x_q=H rho_q` satisfies

```text
H=x_0>=x_1>=...>=x_h>=0.
```

An explicit integral-profile distribution is obtained from one uniform
`U in [0,1)` by

```text
a_q = floor(x_q+U).
```

The same `U` preserves monotonicity, `a_0=H`, and
`E[a_q]=x_q`.  Thus no appeal to a nonintegral profile is needed.

For a fixed profile, coordinate symmetry makes each rank-`m-q` mask and each
rank-`m+q` mask receive load `a_q/N_q`.  Averaging gives `H/W`; total atom
mass `W/H` therefore gives load one in every band rank.  Each atom has reset
length at most `2h+1`, so the fractional reset mass is at most

```text
(W/H)(2h+1).
```

## 6. Tail construction, literal tails, and the proved range

The proposal invokes `TRUNCATED_TAIL_CONSTRUCTION.md`.  Put

```text
h=c sqrt(m),  c=sqrt(omega).
```

Its Theorem 2 constructs one shared word for both tails and proves

```text
L(m,m-h) =
  O((1+c^2) binom(2m,m-h) + c exp(-2c^2) W) = o(W)
```

uniformly when

```text
c -> infinity,   c=o(m^(1/6)).
```

Equivalently, the currently proved rotor range is

```text
omega -> infinity,   omega=o(m^(1/3)).
```

There is no `sqrt(m/omega)` prefactor in this width-order construction.
The submitted assumption `omega=o(m)` is broader than the available uniform
theorem and is therefore not justified as stated.  The clean choice

```text
omega=log m, h=ceil(sqrt(m log m)), H=m-h
```

lies safely in the proved range, gives tail-word length `o(W)`, and also has
`h/H=o(1)`, so the reset ledger remains `o(W)`.

For comparison, if every outside mask were instead appended literally, its
two-sided cardinality divided by `W` has moderate-deviation order

```text
sqrt(m/omega) exp(-omega).
```

That literal quantity can grow for `omega=log log m`.  This is not a
counterexample to the truncated tail word; it is precisely the saving that
the shared Euler construction supplies.

## 7. Exact duplicate--missing identity and the quota requirement

The two rank signs should be explicit.  Let

For `sigma in {-,+}`, put

```text
T_q^sigma = sum_S mu_q^sigma(S),
D_q^sigma = sum_S (mu_q^sigma(S)-1)_+,
M_q^sigma = number of missing masks in that row.
```

Then the exact identity is

```text
M_q^sigma = N_q + D_q^sigma - T_q^sigma.
```

Thus `|T_q^sigma-N_q|=O(W/H)` implies

```text
M_q^sigma <= D_q^sigma + O(W/H).
```

At `q=0` there is one row; at `q>0` there are two.  One may combine the two
duplicate counts, but then the factor two in the error term must be absorbed
explicitly.  Summing gives

```text
Q <= D_0 + sum_(q=1)^h (D_q^-+D_q^+) + O(hW/H).
```

The final packing lemma must therefore require **both**

```text
number of atoms = W/H+o(W/H),
T_q^sigma = N_q+O(W/H) for every q and sign,
sum D_q = o(W).
```

The proposal's final formulation mentions only atom count and duplicate
mass.  Those do not imply the quotas: an undersupplied row can have
`mu_q=0` and hence `D_q=0` while every mask on that row is missing.  The
quota hypothesis in the preceding conditional sentence must be carried into
the formal missing-packing lemma.

Scalar quota rounding is not the hard part.  The common-uniform construction
`a_q=floor(H rho_q+U)` has small support, and integer rounding errors are
polynomial, far below `W/H`.  But ordinary independent sampling at mean load
one produces a positive fraction of collisions and holes.  The unresolved
theorem is a quota-respecting near-disjoint atom packing.

Under that corrected lemma, the implication is valid.  If `A` is the number
of atoms, their total word length is

```text
AH+O(Ah)=W+o(W).
```

The identity above bounds missing band masks by `o(W)`; append them
literally, and use the width-order construction for the two outside tails.
Every atom is an actual MTF word, so no additional factor/pin theorem is
needed inside an atom.

## 8. Exhaustive checker

`scratch/audit_monotone_radius_rotor_suffix.py` independently constructs the
queue, canonical and refined MTF states, initialization word, literal suffix
ORs, and all nonincreasing radius profiles.  Through `m=12` it checked

```text
8,008 local transitions,
16,278 complete profiles,
81,936 exposed chain states.
```

It found no failure.  It also explicitly rejects block collisions, wrong
word lengths, nonliteral exposures, or duplicate masks between chains.

Its SHA-256 is
`3e6d7f89ed7fb57bfdd9bebe373ffedc4c36b76fc35899f0e9353326b1db90e3`.
