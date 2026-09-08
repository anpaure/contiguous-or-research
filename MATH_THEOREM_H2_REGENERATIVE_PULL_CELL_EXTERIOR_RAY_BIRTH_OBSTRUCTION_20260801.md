# Regenerative pull cells: the exterior-ray birth term is indispensable

Date: 2026-08-01

Lane: H2, bounded task birth / sidecar regeneration

Status: exact child-local obstruction and exact exposure-closed state
reduction.  This note does not prove or refute the existence of a globally
chosen regenerative Pascal spine.

## 0. Result

The shortest rotating-hole resident rail and the fixed-bank q1 planting
theorem do **not by themselves certify** bounded task birth, even for one
planted collar.
There is an explicit family in the rank-`m` Johnson layer in which

* one direct seam is replaced by the shortest depth-`h` resident rail;
* both the old rolling-fan path and the new fan--rail--fan path have
  injective lower and upper edge palettes;
* every nonconstant coordinate on the rail cycle has run length exactly
  `h+1`;
* the incidence lift of the whole loss-producing fan--rail--fan path has at
  most `m-2` edges, so it lies inside the scope of the small
  protected-q1-factor theorem; but
* in the displayed local chronology the replacement destroys

  \[
       rs=\left\lfloor\frac{n^2}{4}\right\rfloor,
       \qquad 2(n+h+2)\le m-2
  \tag{0.1}
  \]

  distinct, uniquely witnessed exterior upper targets.  For
  `h=floor(sqrt(m))`, choosing `n=h` gives `Theta(m)` births while the whole
  protected path still has only `O(h)` edges.  Saturating the protected-path
  allowance with `n=floor((m-6)/2)-h` gives `Theta(m^2)` births.

The rail itself still has only the three prefix states and three suffix
states from the shortest-rail theorem.  The quadratic loss is the Cartesian
product of the **external** suffix and prefix ladders.  Consequently, a
bounded regenerative state may not charge only the number of collars, seams,
or ray states.  It must charge targetwise exterior last-witness casualties,
or carry a theorem which dominates that entire Cartesian product by surviving
witnesses.

This gives a sharp omitted debt term in the proposed bounded-birth bridge.
It does not say that a more carefully chosen global q1 completion cannot
restore these targets.

## 1. The family

Let the ground set be `[2m-1]`, let `L` be an `(m-1)`-set, and choose
distinct labels

\[
 a,d_0,c,y\notin L,
 \qquad b\in L.
\tag{1.1}
\]

Put

\[
 F=L+a,\qquad E=L+d_0,\qquad U=L+a+d_0.
\tag{1.2}
\]

Choose pairwise distinct deletion labels

\[
 p_1,\ldots,p_r,q_1,\ldots,q_s,x_0,\ldots,x_{h-1}
       \in L-\{b\}.
\]

Also choose disjoint exterior label sets

\[
 A=\{\alpha_1,\ldots,\alpha_r\},\qquad
 B=\{\beta_1,\ldots,\beta_s\}
\tag{1.3}
\]

outside `U+{c,y}`.  Choose any `n>=2` satisfying
`2(n+h+2)<=m-2`, and set `r=floor(n/2)`, `s=ceil(n/2)`.
Define two rolling Johnson fans

```text
P_i={p_1,...,p_i},   A_i={alpha_1,...,alpha_i},
Q_j={q_1,...,q_j},   B_j={beta_1,...,beta_j}.
```

\[
 X_i=F-P_i+A_i,        Y_j=E-Q_j+B_j.
\tag{1.4}
\]

The old local chronology is

\[
 X_r,\ldots,X_1,F,E,Y_1,\ldots,Y_s.                 \tag{1.5}
\]

Every consecutive pair is Johnson-adjacent.  For `1<=i<=r` and
`1<=j<=s`, the interval from `X_i` to `Y_j` has OR

\[
 T_{ij}=U+\{\alpha_1,\ldots,\alpha_i\}
          +\{\beta_1,\ldots,\beta_j\}.              \tag{1.6}
\]

Each `T_ij` has exactly one interval witness in (1.5).  Indeed, starting
before `X_i` adds the unwanted `alpha_(i+1)`, while starting after `X_i`
loses the required `alpha_i`.  Ending before `Y_j` loses `beta_j`, while
ending after it adds `beta_(j+1)`.  Thus the two required prefixes force
exactly the displayed interval.

Put

\[
 Z=L+a+d_0+y,
 \quad (z_0,z_1,z_2,z_3,\ldots,z_{h+2})
       =(a,y,d_0,x_0,\ldots,x_{h-1}),                \tag{1.7}
\]

and

\[
 V_t=Z-\{z_t,z_{t+1}\},                              \tag{1.8}
\]

with cyclic subscripts.  Thus `V_0=E`, `V_1=F`, and the shortest return
rail is

\[
 F=V_1,V_2,\ldots,V_{h+2},V_0=E.                    \tag{1.9}
\]

Replace the edge `FE` in (1.5) by (1.9).

### Theorem 1.1 (quadratic exterior-ray birth)

Assume `n>=2`.  In the new chronology, none of the `rs` targets `T_ij`
occurs as an interval OR.

#### Proof

Every internal vertex `V_2,...,V_(h+2)` contains `y`, while `F`, `E`, both
fans, and every target `T_ij` avoid `y`.  Any interval containing both an
`alpha` and a `beta` must cross from the left fan to the right fan and hence
contains all internal rail vertices.  Its OR therefore contains `y`, so it
cannot equal `T_ij`.  An interval confined to one side cannot contain both
types of private label.  Thus every `T_ij` is absent.  The balanced split
of `n` gives (0.1).  QED.

### Proposition 1.2 (the local rows remain legal)

The cycle `E,F,V_2,...,V_(h+2),E` has distinct lower edge colours and
distinct upper edge colours.  Its direct edge has colours `(L,U)`, every
other edge avoids them, and every nonconstant coordinate has one cyclic
positive run of length exactly `h+1`.

The whole new fan--rail--fan path has `n+h+2` Johnson edges.  All their lower
q1 colours are distinct, so its incidence lift is one alternating path with
`2(n+h+2)<=m-2` edges.  By the small protected-factor theorem, this entire
path extends to a spanning q1 two-factor of `ML_m`.

#### Proof

The rail assertions are the consecutive-missing-pair identities of the
shortest resident rail.  Along a rolling fan, the edge at step `i` has a
new deletion prefix and a new addition prefix, so its lower colour is unique.
Left-fan colours contain `a`, right-fan colours contain `d_0`, and internal
rail colours contain `y`.  The two boundary rail colours could meet fan
colours only if `x_0=p_1` or `x_(h-1)=q_1`, excluded by the pairwise
distinct choice above.  The same prefix argument separates fan upper
colours; every return-rail upper colour contains `y`, while fan upper colours
do not.  Thus both old and new path palettes are injective.  The edge count
is immediate.  The final assertion is Theorem 2.1 of
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`.
The audit independently replays all identities.  QED.

The extension theorem chooses an arbitrary completion.  Proposition 1.2
therefore proves compatibility with the q1 row, not that every completion
retains the loss in Theorem 1.1 or that no completion can repair it.

## 2. Why three ray states do not bound births

The shortest-rail theorem gives three nested prefix states and three nested
suffix states for the **rail contribution**.  That constant interface is
useful when a complete ladder ticket is already supplied.  It is not a
count of the external targets using the interface.

In (1.5), the left external fragment has the suffix unions

\[
 U+\{\alpha_1,\ldots,\alpha_i\},
\]

and the right external fragment has the prefix additions

\[
 \{\beta_1,\ldots,\beta_j\}.
\]

Their pairwise joins are the `rs` targets (1.6).  One rail state can
therefore support a quadratic target ledger.  Any proposed scalar state
which replaces this ledger by one ``ray ticket'' is unsound unless that
ticket means a complete targetwise ladder certificate.

## 3. The exposure-complete proof-safe state

Fix a prospective same-parity Pascal transition `pi`, including its literal
child chronology, selected q1 completion, residence guards, upper-witness
certificates, and compiler cap state.  Define the following
transition-relative pull cells.

Use literal typed requirement vertices.  First charge to `D` every child row
which is a descendant of an inherited target.  On the remaining child rows,
discard every row protected by a supplied certificate and apply the fixed
priority `E,R,Q,C`: a row admitting more than one diagnosis is placed in its
first class only.  Thus the four residual sets below are a canonical
partition, not four overlapping estimates.

* `D`: inherited carried target defects.
* `E_pi`: old upper targets for which `pi` supplies no certified surviving
  literal witness and no certified new witness.  A surviving witness
  disjoint from the changed support is one sufficient certificate, not the
  definition.  This is a targetwise set; nested ray states are not
  identified.
* `R_pi`: unsealed residence/deadline rows exposed at changed seams and
  endpoints after removing the rows certified inside private resident
  collars.
* `Q_pi`: unmet q1, adjacent-upper, component, opening, and endpoint rows of
  the selected physical host after removing protected rows.
* `C_pi`: a named set of unmatched soft compiler rows under one literal
  trace-guarded common-cap matching which saturates every hard packet task.
  If no such hard-saturating matching exists, put `|C_pi|=infinity` and
  declare `pi` inadmissible.  The cap state and matching belong to the
  certificate; taking the union of edges from different cap states is not
  allowed.

Put

\[
 \Phi_{\rm pull}(S,\pi)=
       |D|+|E_\pi|+|R_\pi|+|Q_\pi|+|C_\pi|.          \tag{3.1}
\]

Endpoint births which are uniform over the transition family may instead be
placed in one fixed constant `b`.

### Theorem 3.1 (exact exposure inequality)

Suppose every inherited carried target has at most four child descendants
and the inherited descendants, four residual classes, and at most `b` fixed
births exhaust the child task ledger.  Then

\[
 |\mathcal U_\pi|
   \le 4|D|+|E_\pi|+|R_\pi|+|Q_\pi|+|C_\pi|+b
   \le 4\Phi_{\rm pull}(S,\pi)+b.                    \tag{3.2}
\]

#### Proof

Charge inherited descendants to `D`.  By definition, every remaining
upper, residence, host, or compiler task lies in its corresponding pull-cell
set, except for the declared fixed bank.  Canonical priority makes these
residual classes disjoint.  Summing gives (3.2).  QED.

Relative to this atomic requirement ledger and the supplied certificates,
this is the smallest rowwise scalarization: it discards every protected row
and every duplicate diagnosis, but it does not identify two unprotected
target rows merely because they traverse the same ray.  A proved complete
compound ticket may of course replace several atomic rows; an informal ray
name may not.  At the child-local ledger level,
Theorem 1.1 shows that deleting `|E_pi|` from (3.1), or replacing it by the
number of ray states, invalidates any dimension-independent inequality
`|U|<=a Phi+b`.  Promotion to a global word additionally requires the
no-alternate-witness certificate stated in Section 4.

For an intrinsic carried state one may put

\[
 \Phi_*(S)=\min_{(\pi,\theta,M)\in {\cal A}_{\rm cert}(S)}
                  \Phi_{\rm pull}(S,\pi,\theta,M),             \tag{3.3}
\]

where `theta` is one literal cap state and `M` is its hard-saturating
matching.  The minimizing transition and all five certificates must be
carried as part of the state.  Set `Phi_*(S)=infinity` when the certified
family is empty.  A minimum over uncertified abstract transitions is not an
admissible recursive invariant.

### Proposition 3.2 (the other prospective terms cannot be dropped)

The exterior coordinate is not the only prospective term.

1. In an odd diamond lift, a clean parent trace `0 1^(d+1) 0` becomes the
   forbidden child trace `0 1^d 0`.  Thus a state which records only current
   residence violations can have value zero while any number of separated
   minimum parent runs create that many child rows.  The proof-safe
   residence coordinate is either one additional run unit or a certified
   actuator hitting every minimum run.  In the authenticated `K15 -> K17`
   fixture there are 1,425 minimum runs, 165 forced unique-colour packets,
   and exact coupled optimum 180.
2. For every `d>=2`, the zero-owner mixed-coatom packet is already clean in
   owner, q1, upper-deck, residence, and path-topology coordinates, but its
   phase-common compiler exposure is

   \[
       X_d=\{A_q,B_q:2\le q\le d\},\qquad |X_d|=2(d-1).         \tag{3.4}
   \]

   Each of the `2(d-1)` named planted chain cells
   `c_q^L,c_q^R` has disjoint phase-zero and phase-one domains.  A common
   compiler of soft deficiency at most `b_c` therefore needs at least
   `2(d-1)-b_c` distinct exterior common neighbours.  Hence a scalar
   omitting prospective common-cap exposure can be `O(1)` while its exact
   exterior compiler requirement is `Omega(d)`.

These are independent of Theorem 1.1.  The first is a residence-margin
obstruction; the second is a one-cap-state Hall obstruction.  The latter
also explains why marginal Hall, or Hall after unioning several cap states,
is not an admissible substitute for `C_pi`.  Like Theorem 1.1, the coatom
row does not forbid a globally prepared exterior ladder; it proves that the
ladder or its deficiency must be present in the transition certificate.

If the compiler is used only at the requested terminal dimension, phase
decoupling permits `C_pi` to be omitted from the *carried* state.  It must
then be charged separately.  For old reference matching `M_0`, complete
literal damage set `D_C`, and deduplicated certified task-cell set
`B={b_i}`, the sharp retained-matching charge is

\[
 \tau_{\rm term}
   =|(D_C\cup B)\cap C(M_0)|.                                  \tag{3.5}
\]

When `D_C` and `B` are disjoint this is the sum of the two separate
intersection counts; without disjointness that sum is only an upper bound.

This is bounded only when complete damage and the number of actually used
task cells are bounded; isolated-ticket legality is insufficient.

## 4. Regeneration verdict

The shortest rail and fixed-bank q1 planting control only parts of (3.1):

* the collar-internal part of `R_pi` is zero;
* its protected q1 incidence rows are zero; and
* the rail's internal all-width deck is explicit.

They do not bound `E_pi`, the unprotected part of `Q_pi`, or `C_pi`.
Let `E_pi^loc` be the targets whose only witness in the displayed local word
is destroyed by the rail.  The family above has one collar and

\[
 |E_\pi^{\rm loc}|=\left\lfloor\frac{n^2}{4}\right\rfloor.
\tag{4.1}
\]

If the surrounding chronology supplies no alternate witness for these named
targets, then the global pull-cell coordinate satisfies
`|E_pi|>=|E_pi^loc|`.  Without that no-alternate-witness condition, (4.1) is
only a local exposure ledger; a global q1 completion may restore some or all
targets.

Therefore these two theorems alone do not certify either
`Phi'<=Phi+C` or a contraction.  A positive bounded-birth theorem must add
at least one of the following:

1. a complete exterior ladder ticket proving `|E_pi|=O(Phi+1)`;
2. a global dominance/star-cover theorem which replaces all vulnerable
   crossing targets simultaneously; or
3. a transition choice theorem whose selected collars avoid every but
   `O(Phi+1)` targetwise last-witness support.

After that, rooted/adjacent-upper host rows and complete compiler damage
still require their own bounds.  The result is a local obstruction to an
omitted debt coordinate, not a no-go for every regenerative Pascal spine.

### Corollary 4.1 (exact surviving contraction inequality)

Suppose a reachable spine proves the exposure estimate

\[
       \widehat\Phi_m:=w({\cal U}_m)\le\lambda\Phi_m+b_0,       \tag{4.2}
\]

with `lambda=4` in the unit-weight specialization of Theorem 3.1.  Here and
below all task totals, service, replay casualties, and `Phi_m` use the same
additive debt weight (unit weight gives ordinary cardinality).  Suppose
further that one guarded Rado batch services weighted rank at least
\(\eta\widehat\Phi_m-\delta\), and that replay creates at most `theta`
times that serviced weight plus `b_1` new carried debt, where
`0<=theta<1`.
Then the exact contraction calculation gives

\[
 \Phi_{m+1}\le\rho\Phi_m+B_0,
 \quad
 \rho=\lambda[1-(1-\theta)\eta],
 \quad
 B_0=[1-(1-\theta)\eta]b_0+(1-\theta)\delta+b_1.              \tag{4.3}
\]

Thus a uniform bound follows when `rho<1`; with `lambda=4` this requires

\[
                       (1-\theta)\eta>\frac34.                 \tag{4.4}
\]

By contrast, iterating `Phi_(m+1)<=Phi_m+C` with `C>0` gives only a linear
bound and is not a bounded-sidecar theorem.  The resident rail and fixed-H
q1 planting establish neither (4.2) with the omitted coordinates removed
nor the service/casualty inequality in (4.3).  The precise surviving gate is
therefore a globally exposure-closed transition plus sufficiently strong
guarded service and bounded complete damage, not another local rail or q1
embedding theorem.

## 5. Audit

Run

```text
python3 scratch/audit_h2_regenerative_pull_cell_exterior_ray_birth_20260801.py
```

The dependency-free replay checks the maximal protected-path regime for
`25<=m<=80` and the fixed-H `O(h)` protected-path regime for `36<=m<=100`,
always with `h=floor(sqrt(m))`.  It verifies ranks, every Johnson adjacency, injectivity
of both q1 palettes on the whole new path, injectivity of the complete
rail-cycle lower and upper palettes, exact cyclic residence, the exact
incidence-lift protected-factor threshold, uniqueness of all old `T_ij`
witnesses, and absence of every `T_ij` after the rail replacement.

No Joos--Mubayi--Smith theorem is used.

The residence and compiler rows in Proposition 3.2 are the exact results of
`MATH_THEOREM_ODD_DIAMOND_RESIDENCE_TAX_20260731.md` and
`MATH_THEOREM_K_ZERO_OWNER_COATOM_U5_REGENERATIVE_RECURRENCE_20260801.md`.
The terminal charge (3.5) is the retained-matching form of
`MATH_THEOREM_BOUNDED_COMPILER_EVICTION_AND_PHASE_DECOUPLING_20260801.md`.
Equations (4.3)--(4.4) specialize the authenticated uniform-contraction
calculation in
`MATH_THEOREM_R_K17_GREEDY296_GUARDED_RADO_CUT_AND_UNIFORM_CONTRACTION_20260731.md`.
