# The double-fan affine Hall obstruction

Date: 2026-07-29  
Scope: fixed resident/q1 overlay systems; exact linear theorem

## 1. Abstract lemma

Let

\[
 a,b,c,d,p,q,x,y,z\ge0
\]

satisfy the following nine inequalities:

\[
\begin{array}{rclcrcl}
x-a&\le&0,                 && z-p&\le&0,\\
b&\le&0,                   && z-q&\le&0,\\
a+c-b-d&\le&0,             && p+q-x-z&\le&0,\\
d-c&\le&0,                 && y&\le&0,\\
&&&& -x-y-z&\le&-1.
\end{array}                                      \tag{1.1}
\]

Then (1.1) is infeasible, even over the nonnegative reals.

Indeed, summing the four inequalities in the left packet gives

\[
                         x\le0.                  \tag{1.2}
\]

In the right packet, `z<=p`, `z<=q`, and
`p+q<=x+z` give `z<=x`.  The last two rows give
`x+z>=1`; hence

\[
                         2x\ge1,                 \tag{1.3}
\]

contradicting (1.2).  Equivalently, twice the sum of the left packet
plus the sum of the right packet is the Farkas certificate

\[
                         0\le-1.
\]

No Boolean assumption is used.  Therefore the lemma rules out the LP
relaxation as well as the integral overlay.

## 2. The common `k=16` instance

For the fixed fully resident endpoint

```text
scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
```

all three radius-four q1-perfect, zero-unit-core endpoints contain the same
length-two residence motif

```text
coordinate 11
closure {(62050,64034), (62514,63538), (63538,64034)}.
```

The variable correspondence is

```text
x = remove (63538,64034)      a = add    (63526,64546)
y = remove (62050,64034)      b = remove (63526,63750)
z = remove (62514,63538)      c = add    (61486,63526)
                               d = remove (59438,63526)
                               p = add    (61554,63538)
                               q = add    (48178,63538).
```

The four rows in the left packet are, respectively,

```text
lower 63522, upper 63782, vertex-red<=blue 63526, upper 63534.
```

The five rows in the right packet are

```text
lower 61490, upper 64562, vertex-red<=blue 63538,
lower 61986, and the coordinate-11 residence motif.
```

Literal reconstruction verifies that these rows are exactly (1.1), with no
omitted provider or incidence variable.  The nine-row subsystem is
inclusion-minimal: deleting any one row admits an explicit Boolean witness.
The complete replay is

```text
scratch/audit_k16_three_zero_unit_candidates_common_affine_core_20260729.py
scratch/k16_three_zero_unit_candidates_common_affine_core_20260729.audit.json
```

## 3. Consequences for the search

1. Eliminating all unit-propagation cores is insufficient.  The obstruction
   appears only after summing capacities across two local fans.
2. Any trade confined away from the three motif edges and the eight support
   rows leaves the contradiction intact, regardless of its effect on other
   residence motifs.
3. A sound local search potential must count double-fan affine cores (or use
   a failed-literal/Farkas separator), not merely individually forced motifs.
4. The next admissible trade must delete or recolour at least one edge in the
   displayed motif/support packet, or change the resident endpoint itself.

This is an endpoint-specific no-go, not a theorem against PBBS factors or
against `nu(16)=12873`.
