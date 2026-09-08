# Independent audit of the full-line-deficit deliverables

## Verdict

The resolution contains one useful new fixed-bottom estimate, but it does
not establish its advertised bottom-threshold optimality, scalar sharpness,
or unique minimal missing lemma.  The companion self-audit incorrectly marks
those claims as proved.

## Statements that survive

1. **Gap partition (Lemma 3.1), with a convention repair.**  If
   `gamma_term` is the combined mass of both linear end gaps, then
   
   ```text
   delta = gamma_int + gamma_term + o(1).
   ```
   
   This follows directly by partitioning the word into selected plateau
   intervals, internal gaps, and the two boundary gaps.  It should not be
   attributed to the contraction identity.

2. **Desert identity (Lemma 4.1).**  Hamiltonity and the definition of the
   selected-line desert give
   
   ```text
   D_a/a^2 = gamma_des + o(1),   gamma_des <= delta.
   ```
   
   This does not identify desert mass with internal-gap mass and does not by
   itself supply the prose "covered-gap rebate."

3. **Refined fixed-bottom estimate (Theorem 5.1).**  Replacing the crude
   wedge error `sqrt(6 delta)` by `sqrt(6 gamma_des)` is legitimate.  The
   algebra gives
   
   ```text
   U(1+) <= 15/4 + (5/4)sqrt(6 gamma_des)
                     + 3 gamma_int - (3/2)delta
          <= 15/4 + (5/4)sqrt(6 gamma_des)+(3/2)delta.
   ```
   
   Hence the stated exclusion frontier
   
   ```text
   gamma_des < (1-6delta)^2/150,   delta<1/6
   ```
   
   is valid.

4. **Level-tension bounds (Lemma 6.1).**  Lebesgue domination gives
   `tau_A >= sum A_d^2/2`.  Pushing two measures to the upper ends of
   `[0,1]` gives the exact corner minimum
   `((A_d+A_e-1)_+)^2/2` for their `t+u<=1` intersection.

5. **Conditional arithmetic of Theorem 9.1.**  If its unproved Lemma M held
   with the stated sign and definition, the optimization is correct.  At
   `delta_1=1/24` the sufficient constant is `12.5`, not `12`.

## First invalid inference

Theorem 7.1 does not follow from monotonicity of `delta(c)` and
`gamma_des(c)`.  The claimed shift

```text
3c-3+2e(c)
```

does not vanish at `c=1+` unless `e(1)=0`.  The correct baseline difference
is

```text
3(c-1)+2(e(c)-e(1)),
```

whose derivative is `3-2f(c)` and can be negative.  For the broad profile
`mu=2*1_[1,2]`, the function `3c+2(2-c)^2` decreases initially.  Therefore
bottom-threshold optimality and "no threshold sweep helps" must be
retracted.

## The claimed scalar extremizer is inconsistent

The two descriptions of its gap law cannot simultaneously make the sharp
gap row and all moment rows tight.  Under the asserted sharp
`(p,s,z)=(2,2,1)` gap atoms, the crossing equality `C=2A` forces
`p+s=3` on absorbed mass.  If `delta` is the sharp-gap mass and the remaining
nonabsorbed zero-gap mass is `R=f-A-delta`, the total `p+s` moment is at
least

```text
3A+4delta+2R = A+2f+2delta = 6,
```

while the required moment is `2ell=6-2delta`.  This is impossible for
`delta>0`.  Thus the file does not certify sharpness against the listed
constraint families.

## Status of Lemma M

Lemma M remains unproved, and `gamma_cov` is used with incompatible meanings:
first as the internal part of desert mass, later as `delta-gamma_des`.
Moreover, dangerous-list self-closure supplies the separate stronger saving
`phi_c^star`; hence the claim that Lemma M is the unique or minimal next
lemma is obsolete before that stronger functional is optimized.

The authoritative conclusion is therefore: retain Theorem 5.1 and its
frontier; retract Theorem 7.1, the scalar sharpness claim, and the asserted
minimality of Lemma M.
