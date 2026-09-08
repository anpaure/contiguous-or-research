# Audit of the left-anchored global-sharing reduction

## Verdict

**PASS as a conditional transfer theorem, with two clarifications.**

For intervals `I_i=[i,rho_i]` with strictly increasing right endpoints,
individual central pin survival really does imply the required pin survival
in every nonempty consecutive common core.  This implication is special to
the ordered left-anchored schedule and needs a proof; it is false for general
interval systems.  With that lemma supplied, the maximal-factor construction
covers every assumed upper join and lower meet in at most `L+D` positions.

This remains a reduction, not the missing construction.  The hypotheses of
upper completeness, lower completeness, and pins have not been achieved with
subcubic excess.

Two statements should be normalized:

1. The actual used physical length is `rho_L` (after deleting an unused
   tail), and `rho_L<=L+D`.  The expression `L+rho_L-L` in the proposed final
   lemma is just `rho_L`; it should be written as either `rho_L` or the
   sufficient bound `L+D`.
2. The finite exact-once dual-simplex evidence concerns the *required
   four-box subfamily*.  It must not be read as an exact-once theorem for all
   feasible dual triples: the complete dual family already fails exact-once
   at `D(1,1)`.

## 1. Linked unions and common cores

Strictly increasing integer right endpoints give

```text
I_p union ... union I_q = [p,rho_q]
I_p intersect ... intersect I_q = [q,rho_p].
```

The first equality uses overlap or adjacency: `rho_i>=i`, while the next
interval begins at `i+1`.  The second follows because starts and ends are both
in increasing order.  The core is nonempty exactly when `q<=rho_p`.

## 2. Maximal factor and the missing core lemma

For one threshold atom `b`, let

```text
N_b = union_(i:b notin C_i) I_i,
Z_b = [L+D] minus N_b.
```

At every used position `j`, the maximal factor contains `b` exactly when
`j in Z_b`.  Hence the assumed central pin condition is precisely what makes
the union over each `I_i` equal `C_i`.

Now suppose `b` belongs to every `C_p,...,C_q` and the common core
`J=[q,rho_p]` is nonempty.  If `J` were contained in `N_b`, one connected
component of the union of negative intervals would cover all of `J`.
Negative indices cannot lie in `[p,q]`.  Intervals with indices below `p`
have right endpoints strictly below `rho_p`, so they cannot cover the right
end of `J`; intervals with indices above `q` start strictly after `q`, so
they cannot cover its left end.  The covering component must therefore join
at least one negative interval from each side.  Its connected hull then
contains every complete positive interval `I_i`, `p<=i<=q`, contradicting
the central pin condition.

Thus

```text
J intersect Z_b is nonempty
```

for every atom in the consecutive meet.  Atoms outside the meet are absent
from all positions of the core because at least one of its central intervals
omits them.  Therefore the exact identity is

```text
join_(j in J) A_j^max = meet_(i=p)^q C_i.
```

This proves the lower step that was asserted but not demonstrated in the
submitted proof.

## 3. Upper step

If an upper target is `C_p join ... join C_q`, linkedness gives one physical
interval `[p,rho_q]`.  Its factor union is the join of the central window
unions and hence exactly the target.  Together with the core lemma, all three
levels—upper, central, and lower—are realized.

Positions after `rho_L` occur in no central interval and may be deleted, so
the actual word has length at most `rho_L<=L+D`.

## 4. Dual-simplex and spine scope

The primal truncated-simplex sector and its exact-once perimeter ordering are
already audited.  The complementary four-box sector reduces to the relevant
dual extrema `(max d,max a,min(d+a))`.  A uniform alphabet-plus-subquadratic
word for that relevant domain, together with a compatible increasing-right
schedule, lower meets, and pins, would be sufficient.  No such uniform word
or schedule is proved.

The descending-spine obstruction is valid for the stated canonical
architecture.  Assigned arms on one pass must form a chain in the order

```text
(u,x) <= (v,y) iff u<=v and x>=y.
```

The diagonal arms `(2,1),...,(R-1,R-2)` form an antichain, forcing distinct
passes.  Even if passes are shortened, the pass assigned to `(u,u-1)` must
retain all peak starts for `r>u`, so the total peak requirement is at least

```text
sum_(u=2)^(R-1) (R-u) = Omega(R^2).
```

Thus merely sharing canonical descending peak spines cannot yield the desired
subquadratic triangular excess.

## 5. Remaining status

The proposed factorable dual-sector theorem is a correct sufficient target.
It has not been constructed, for balanced or uniformly unbalanced boxes.
Consequently the established global upper coefficient is unchanged.

## 6. Exhaustive regression

The checker

```text
scratch/audit_left_anchored_global_sharing.py
```

enumerates every increasing-right schedule with `L<=8`, `D<=5` and every
binary coordinate-labeling.  For every labeling satisfying all individual
central pins, it verifies every central window and every nonempty consecutive
meet core in the maximal factor.  It reports

```text
PASS schedules=4998 positive_nonempty_cores=5396041 length<=8 delay<=5
```

Its SHA-256 is

```text
d4fd09b162d0cfd26ada672469beb88561a3b6f89e98e9eb0ebf6655b23fc764.
```
