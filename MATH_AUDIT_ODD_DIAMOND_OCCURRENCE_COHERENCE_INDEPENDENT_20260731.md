# Independent audit of odd-diamond occurrence coherence

Date: 2026-07-31  
Status: GO with explicit marginal-versus-joint quantifiers

## Exact general ledger

For a one-occurrence-per-(Z) transversal (S), let (e_Z\in S) be the
selected occurrence in fibre (Z), and let (u_Z) count the occurrences in
that fibre which uniquely provide their parent upper union.  The actual
number of deleted upper-unique provider edges is

\[
 D_U(S)=\sum_Z\left(u_Z-
       1_{\{e_Z\text{ is upper-unique}\}}\right).             \tag{1}
\]

Consequently

\[
             \min_S D_U(S)=\sum_Z(u_Z-1)^+.                   \tag{2}
\]

Equation (2) is an unconstrained marginal minimum.  It is not the debt of
every transversal and cannot be added to a separately optimized residence
minimum.  The proof is fibrewise: at most one provider survives in a fibre,
and retaining one whenever (u_Z>0) attains the bound.

The exact recursive state must therefore retain the actual one-hot vector
(S), the identity set of lost/surviving upper witnesses, the residence
packet indicators or physical compensators, and the induced macro endpoint
demands.  The endpoint `b`-flow begins only after this joint state is fixed.

Deleted internal providers may be recreated at ports, so neither (1) nor
(2) is a final child upper-hole lower bound.

## Independent finite replay

For the authenticated `6390+45` parent, direct replay gives

```text
upper multiplicity       1^3675 2^1230 3^100
depth-two multiplicity   1^3630 2^1320 3^55
u_Z profile              0^1835 1^2685 2^465 3^20
marginal provider debt   505
exact residence debt     180
```

For `scratch/k15_octahedral_translation_descent_r2.factor.json`, it gives

```text
component lengths        2355,1680,1440,840,75,45
u_Z profile              0^1735 1^2865 2^405
marginal provider debt   405
exact residence debt     150
```

The `150` claim now has an independent exact certificate.  A literal
one-occurrence witness satisfies the bound-`150` formula and replays with
150 internal `0-111-0` packets.  The bound-`149` CNF has 22,245 variables
and 42,912 clauses; Kissat returns UNSAT and `drat-trim` independently
verifies the retained proof with a 904-clause core and 2,455 resolution
steps.

The audit artifacts are

```text
scratch/build_odd_diamond_depth3_residence_bound_cnf_20260731.py
scratch/audit_odd_diamond_occurrence_coherence_independent_20260731.py
scratch/odd_diamond_occurrence_coherence_independent_20260731.audit.json
scratch/odd_diamond_occurrence_coherence_octa_r2_bound149_20260731.cnf
scratch/odd_diamond_occurrence_coherence_octa_r2_bound149_20260731.drat
scratch/odd_diamond_occurrence_coherence_octa_r2_bound149_20260731.dratcheck.txt
scratch/odd_diamond_occurrence_coherence_octa_r2_bound150_20260731.cnf
scratch/odd_diamond_occurrence_coherence_octa_r2_bound150_20260731.kissat.txt
```

Scope is limited to the two authenticated parent factors and the flat
depth-three occurrence-transversal macro architecture.  No global `K17`,
nonflat-compiler, or all-(k) obstruction is claimed.
