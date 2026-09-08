# Independent-style audit of the onion named-cell Hall theorem

## Verdict

**PASS.**  The confinement lemma, the general named-cell family inclusion,
all four Type-I/Type-II specializations, and the coefficients `97+z` and
`96+z` are valid.  The induced selected-width cuts `96+z`, `95+z`, and
`96+z` are also valid.  The result is genuinely stronger than a scalar blocker
row because it restricts target witnesses to branch-specific physical cells
and tests their actual OR ranks.

## 1. Confinement

For `q` incomparable equal-rank witnesses in `q+t` positions, sorted left
and right endpoints both increase.  The `i`th interval lies in `[i,i+t]`.
Every interval `[a,b]` of length at least `t+1` has `a<=q` and contains
`I_a`.  Thus its OR has rank at least the selected rank.  There is no endpoint
or boundary exception.

The checker exhausts every possible pair of increasing endpoint sets for
`0<=q<=6`, `0<=t<=3`, retaining every legal interval pairing, and verifies
this containment statement directly.

## 2. Component assignment

A witness for a target below rank `r` cannot contain a literal rank-`r`
entry.  It is therefore wholly inside one low component.  A nonliteral
rank-`r` target likewise cannot contain any literal rank-`r` entry: a
rank-`r` entry contained in its OR would have to equal the target, contrary
to nonliterality.  Hence all selected nonliteral active-rank witnesses can be
assigned to the low components exactly as used in the slack calculation.

Once a component has slack `t_j`, the confinement lemma proves the family
inclusion, not just its cardinality.  Counting distinct physical cells gives
the displayed Hall row; duplicate OR values only make the necessary
condition stronger.

## 3. Type-I arithmetic

After the unique literal six-set is deleted, the suffix has 464 positions.
Its `z` literal five-sets are distinct, leaving a low core of length
`464-z`.  Exactly `462-z` rank-five targets remain nonliteral.  Thus the core
slack is two.  At cutoff four every core singleton qualifies, giving

```text
E_4 >= 561-(464-z)=97+z.
```

Of the `|C|-1` pair cells, at least `E_4` are unavailable to a rank-five
witness.  The `|C|-2` nonliteral rank-five witnesses all have length two or
three.  Therefore at least `E_4-1>=96+z` are triples.  This is a genuine
coupling between actual pair-cell ORs and the two-sided selected endpoint
width profile.

No use is made of a fixed derivative row or a preselected rank-five path.

## 4. Type-II arithmetic

Deleting `h` literal occurrences leaves `465-h` positions and `462-z`
nonliteral values, so total slack is `3-(h-z)=3-delta`.  The already audited
stability row `delta+s<=2`, positivity of component slacks, and `s>=1` leave
exactly the three cases in the theorem.

For `(delta,s)=(0,2)`, the singleton pool has size `465-z` and only adjacent
pairs of the slack-two component can add lower targets.  Therefore

```text
E_4^(2)>=561-(465-z)=96+z,
|C^(2)|>=E_4^(2)+1>=97+z.
```

The slack-two component has `|C^(2)|-2` selected rank-five witnesses and at
most `|C^(2)|-1-E_4^(2)` available rank-five pair cells.  Hence at least
`E_4^(2)-1>=95+z` witnesses are triples.  The one-component duplicate branch
gives the Type-I coefficient `96+z` by the identical calculation.

The other two coefficient rows follow from singleton pools `465-z` and
`464-z`, respectively.  All finite arithmetic is reproduced by
`scratch/check_k11_onion_named_cell_hall.py`.

## 5. Scope

This is a necessary branch cut, not a contradiction.  It does not assert
that qualifying cells have distinct OR values.  The stronger family
inclusion says every target value must occur; the scalar rows count candidate
cells and permit collisions, as a safe relaxation.

The theorem is outside the endpoint-blocker barrier's scope.  That barrier
assigns a length cap targetwise and counts all physical intervals below the
cap.  The present result removes cells of allowed global length according to
their component ownership and actual OR value.  It is therefore a first
genuinely named-cell consequence of the onion architecture.
