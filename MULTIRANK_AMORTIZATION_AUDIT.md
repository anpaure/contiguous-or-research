# Audit of simultaneous multirank amortization

## Verdict

The common-zeta formulation, simultaneous credit-row budget, dead-row
criterion, and local incidence inequality in `MULTIRANK_AMORTIZATION.md` are
valid.  The exact checker reproduces all displayed finite values.  The
negative conclusion has the correct scope: it proves feasibility only of a
necessary fractional relaxation, not existence of an OR word or even of an
integer coordinate-labelled support family.

## 1. Credit rows

For rank `r`, there are exactly `M_r=C(k,r)` physical windows of length
`ell_r=n-M_r+1`.  The amortized theorem supplies
`p_R+q_R^(r)>=c_r`.  If two ranks have the same `M_r`, their `q` variables
refer to the same physical row.  Each window has one OR value, so summing all
exact-rank counts in that row is at most `M_r`.  This proves (3.4) and (3.5).

The cap `C_s(n)` is the minimum of valid containment caps, hence remains
valid.  If `ell_r>C_r(n)`, an exact-rank-`r` window in the credit row is
impossible and `q_R^(r)=0`.  The dead-row pointwise upgrade is therefore
sound.

## 2. Zeta/window incidence

For fixed `T` and `r<=|T|`, summing `p_R` over the `r`-subsets of `T` counts
position `i` exactly `C(|T|-|A_i|,r-|A_i|)` times when `A_i subseteq T`.
Summing the `q` variables counts distinct length-`ell_r` windows whose exact
OR is an `r`-subset of `T`; these are a subfamily of all such windows lying
inside `P_T`.  This proves (4.1).

For a binary support of total size `p_T`, merging runs cannot decrease the
number of fixed-length internal windows, proving
`W_ell(T)<=(p_T-ell+1)_+`.  The binomial coefficient in (4.1) is maximized by
the smallest possible nonempty entry rank, namely one.  Equation (4.2)
follows.

## 3. LP symmetry and filtration scope

All zeta and row-budget constraints are invariant under coordinate
permutations and convex after linearizing `(c-p)_+`.  Averaging a fractional
solution over `S_k` is legitimate and gives (5.4).  This argument does not
preserve integrality, which is why the output is explicitly called a
fractional certificate.

`RANK_FILTRATION_STABILITY_AUDIT.md` does **not** force zero literal rank-`r`
mass: it permits distinct rank-`r` literals in boundary blocks.  The checker
voluntarily moves the first-record rank mass down by one only to exhibit an
especially simple fractional certificate.  That move preserves the
cumulative filtration inequalities, increases every support-zeta
coefficient, and realizes the allowed zero-boundary, one-component special
case.  It is not asserted to be necessary.

The `k=6` zero-literal conclusion has a separate justification: its residual
`sigma_3` is zero, and the audited boundary-mass inequality
`d_3 z<=sigma_3` forces `z=0` there.

## 4. Mechanical verification

Running

```bash
python3 scratch/check_multirank_amortization.py
```

checks with Python exact integers and `Fraction` arithmetic:

* `B(k)`, all active `(d_r,ell_r,c_r)` rows, and all simultaneous caps;
* feasibility of the displayed symmetric profiles for `1<=k<20`;
* the live-rank classification through `k=200`;
* larger rational checkpoints `20,25,50,100,200`;
* domination of (4.2) by the nested cap-and-run bound through `k=19`;
* the complete `k=6` support and adjacent-window equalities on the certified
  word.

The checker passed in about 2.2 seconds on the audit machine.

## 5. Scope guardrails

The calculation does **not** establish any of the following:

* an integer solution of the coordinate-labelled ILP for an open dimension;
* compatible physical ordering of the proposed entry multiset;
* realization of the abstract `q` credits by actual support runs;
* endpoint-chain orthogonality or coordinate pin survival;
* `nu(k)=B(k)` for any previously open `k`.

Accordingly, the correct conclusion is that simultaneous amortized zeta
moments do not refute the conjectured lengths at the tested fractional level.
The remaining obstruction must use non-symmetric deficiency correlations or
ordered/pinning geometry.
