# Adversarial audit of core-local amortization and pin coupling

## Verdict

**PASS.**  The support split, two-interface credit lemma, core-local capacity
inequality, nonlinear deficiency budget, moment-tight boundary penalty, and
consecutive-facet refinement are valid under the exact boundary--core
hypotheses stated in `AMORTIZED_PIN_COUPLING.md`.

The strongest unconditional `k=11` consequences are

\[
 6a_{28}+4a_{29}+2a_{30}+a_{31}\le462
\]

in the no-six-set branch, and the exact corrected inequality (5.4) in the
one-endpoint-six-set branch.  Neither is contradictory.

## 1. Boundary support and outside-core windows

Every peeled boundary entry is a distinct `r`-set.  Its contribution to the
support of another `r`-set is therefore zero, and its contribution to its own
support is one.  This proves the exact support split without an incidence
multiplicity error.

A rank-`r` length-`d+1` window touching a boundary entry `T` must have OR
exactly `T`; otherwise it contains two distinct comparable-by-union rank-`r`
values, forcing rank above `r`.  Since `d+1>=2`, it cannot lie within a
boundary block.  To meet the core while containing only one boundary entry,
it must start (or end) at the interface entry, and that physical window is
unique.  Distinctness of all boundary values prevents one `R` from receiving
credits from both interfaces.  Thus `x_R in {0,1}`, supported on at most two
values, is correct.

The restriction `r<k` matters when excluding an interval spanning both
boundary blocks.  It is explicitly imposed in the note.  Such an interval
contains the coordinate-complete core and has OR `[k]`.

## 2. Core-local capacity

Every nonempty proper subset of an `r`-set has rank below `r` and therefore
has a witness wholly in the peeled core.  The global containment theorem
bounds that witness by length `d`; it does not need to be a shortest witness.
Distinct targets use distinct physical intervals.

The maximal core support runs have length at most `d+1`.  A length-`d+1`
core run has OR rank at least `r`, is contained in `R`, and hence has OR
exactly `R`.  Conversely a core window of that length and OR `R` exhausts its
support run.  The same quadratic run inequality used in the audited
amortized theorem therefore yields

\[
 (d+1)p_R^C+(d-1)q_R^C\ge2(2^r-2).
\]

The core length is `M+d-h`, so it has exactly `M-h` windows of length
`d+1`.  This confirms the global credit budget.  Taking the ceiling after
isolating `q_R^C` gives `g_{r,d}` with the correct inequality direction.

The second term in (4.4) is also safe: the full theorem gives
`p_R+q_R>=c`, and the exact splits give

\[
 q_R^C\ge c-p_R^C-b_R-x_R.
\]

Taking the pointwise maximum of two simultaneous lower bounds and summing
against one physical credit budget does not double-charge a window.

## 3. The eleven-bit coefficients

At `d=3,r=6`, the core inequality is `2p+q>=62`.  The original full-subcube
inequality is `p+q>=32` away from a boundary correction.  Their pointwise
maximum at support sizes `28,29,30,31` is respectively

```text
6, 4, 2, 1.
```

There are 462 core length-four windows in Case I, proving (5.3).

In Case II there are 461 core length-four windows.  The literal value `T`
has one support position outside the core and at most one crossing credit.
At core support sizes 28, 29, and 30, the proper-subcube requirements 6, 4,
and 2 dominate the weakened full-subcube requirement.  At size 31, `T`
requires zero rather than one core credit.  Hence subtracting exactly
`1_{p_T^C=31}` from the uniform coefficient sum is correct.

The pointwise floor `q_R^C<=floor(p_R^C/4)` rules out support at most 27 and
justifies omitting smaller indices from the displayed cuts.

## 4. Tight-moment penalty

Let `s_R=p_R+q_R-c` for a literal boundary value.  Substitution into the
core inequality gives exactly

\[
 (d+1)s_R\ge
 d-1-\varepsilon+(d+1)x_R+2q_R^C.
\]

Also

\[
 \Delta=(M-\sum q_R)+\sum s_R
\]

is an exact identity, and each term on the right is nonnegative.  Therefore
`epsilon<=d-2` charges at least one unit per boundary value.  At `Delta=0`,
the only possible boundary profile has no interface credit, no core long
credit, and `epsilon>=d-1`.

For the `k=11` tight branch, the independently audited run arithmetic gives
`q_U=1` for all 462 six-sets.  This is incompatible with the required
`q_T=0` of any literal boundary value, so `h=0`.  The note correctly warns
that cumulative rank truncation already makes this tight scalar branch empty
at the actual checkpoint.

## 5. Consecutive-facet refinement

In an inner rank-`r-1` boundary--core decomposition, a nonliteral
rank-`r-1` target cannot use an interval touching a literal boundary facet:
that interval would contain a distinct incomparable set of the same rank.
It must therefore be represented in the deeper core.  All still-lower
targets are there by the inner theorem.  Exactly `t_R` proper subsets of `R`
are removed from the deep-core target demand, giving (7.4).

The `t_R` boundary positions themselves belong to the support of `R`, so
`p_R^C=p_R^D+t_R`.  Substitution changes the right side by
`(d+1)t_R-2t_R=(d-1)t_R`, proving (7.5).  Each `(r-1)`-set has exactly
`k-r+1` rank-`r` supersets, which verifies the incidence total.

At `k=11`, division of (7.4) by two gives

\[
 2p_U^D+q_U^D\ge62-t_U.
\]

The deep core has length `464-h_5`, hence `461-h_5` length-four windows.
All constants in (7.8)--(7.11) are correct.

## 6. Scope

The theorem controls only how much long-window credit is necessary.  It does
not say that different `R`-sets can realize their demanded windows with
compatible coordinate pins, nor does it force a fixed-rank row unless a
separate tightness argument applies.  High-support profiles make all the new
lower-tail demands vanish, so feasibility of the numerical cuts is not an
existence theorem.

No current exact-value bound changes.

The independent executable check

```text
python3 scratch/check_amortized_pin_coupling.py
```

passes on every archived exact word and on the symbolic `k=11` tables.
