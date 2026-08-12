# Cross-audit of the quaternary-octagon OR interface

Date: 2026-08-01  
Status: corrected exact local theorem; global exact-factor implication open.

Audited files:

* `MATH_THEOREM_AD_QUATERNARY_OCTAGON_EXTERIOR_RAY_AND_RESIDENCE_INTERFACE_20260801.md`;
* `MATH_AUDIT_AD_QUATERNARY_OCTAGON_EXTERIOR_GUARD_COUNTEREXAMPLE_20260801.md`.

## 1. Deck verdict

For

\[
 X=(A_1,V_1,\ldots,V_0,B_3),\qquad Q=Z+a_3,
\]

the exact formulas are

\[
 \mathcal P(X)=\{Z-\{a_0,y\},Z-y,Z,Q\},
\]

\[
 \mathcal S(X)=\{B_3,Q-\{a_1,y\},Q-a_1,Q\},
\]

\[
 \mathcal I_{\ge3}(X)=\{Z,Q-a_1,Q\}.
\]

The first two are strict chains.  The third is not: `Z` and `Q-a_1` are
incomparable.  The source wording and quantifier have been corrected to
`1<=h<=m-2`.

## 2. Residence correction

The two collar flags

\[
 \Lambda_t=\{z,x_0,\ldots,x_{h-t-1}\},\qquad
 P_t=\{a_3,x_t,\ldots,x_{h-1}\}
\]

are necessary and sufficient only after imposing ordinary off-end
cleanliness: a positive exterior run on a coordinate absent from `A_1`
(respectively `B_3`) must have length zero or at least `h+1`, unless it
remains globally clipped.  This condition is necessary because such a run
terminates at the new zero and becomes internal.  Under it, the only
remaining deficits are exactly `h,h-j-1` on the left and `h,j` on the
right, proving the two flag formulas.

The literal `m=5,h=1` fixture survives the correction: its sole left
off-end run is globally clipped, and its sole right off-end run has length
two.

## 3. Exact rolling-fan quantifier

On a `2m`-point ground set, `|Q|=m+3`; after reserving `a_2`, the two
private donor banks exist under

\[
                              r+s\le m-4.
\]

There are explicit simple Johnson paths.  From `B_1`, replace `a_1` by
`ell_1`, introduce the other `ell` labels by deleting temporary labels of
`S`, replace `a_2` by `z`, restore the temporary labels in reverse order,
and replace `ell_1` by `a_3`.  This ends at `A_3`; the turn at `z` prevents
repeated owners.  The analogous path from `B_3` to `A_2` uses the second
bank.  Their selected suffix/prefix profiles give `rs` distinct old donor
grid targets, all omitting `a_1`; every new interval seeing both banks
passes through `B_1` and contains `a_1`.

The dependency-free cross-audit checks all 220 parameter triples with
`6<=m<=15` and `r+s<=m-4`.

## 4. Decisive scope boundary

The rolling fans and the sixteen-owner fixture establish independence from
the **local octagon** four-resource identity.  They are not globally
lower/upper-rainbow four-resource factors.  Therefore they do not prove
that the donor-grid obstruction survives the fixed-`H` exact-factor
extension theorem.  The exact surviving statement is:

\[
 \boxed{\text{local collar data do not repay the donor-swap grid;}\quad
        \text{ambient-factor automatic repayment remains open}.}
\]

Common-cap compilation remains wholly separate.

## 5. Replay

Run

```text
python3 scratch/audit_ad_octagon_interface_crossaudit_20260801.py
```

It reports

```text
PASS_AD_OCTAGON_INTERFACE_CROSSAUDIT
payload_sha256=b552653ca973f92db1e3c18dc230ea932e9b07edf00730e62cc129cab052cc50
```

