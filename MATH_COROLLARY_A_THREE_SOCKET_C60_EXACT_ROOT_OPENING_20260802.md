# Exact root opening of the three-socket `C60`

**Date:** 2026-08-02  
**Status:** exact local corollary to
`MATH_THEOREM_A_THREE_SOCKET_B5_C10_BOOLEAN_C6_FUSION_20260802.md`.
It opens the residual `C60` with one further Boolean `C6`.  It is not a
global planting, history, residence, upper-shadow, source, or compiler
theorem.

## 1. Construction

Assume `m>=6` and retain the notation of the three-socket theorem.  Let its
first fusion use `X=d_0`.  Choose another `d`-type pair `Y=d_1`, so the
vertical edge in socket 1

\[
 e=(L,L+\{\gamma,\delta\},L+\gamma,L+\delta),
 \qquad L=C_0+\alpha+Y                              \tag{1.1}
\]

is untouched and lies on the final directed `C60`.

Choose `q in C_0` and a fresh coordinate

\[
 c\notin C_0\cup K\cup\{\alpha,\beta,\gamma,\delta\}.
                                                               \tag{1.2}
\]

These choices exist: `C_0` is nonempty and the complete support has size
`m+6<=2m`.  Put `T=L-q`, and adjoin the two old exterior atoms

\[
\begin{aligned}
o_1&=(T+\delta, T+\{\gamma,\delta,c\},
                  T+\{\gamma,\delta\}, T+\{\delta,c\}),\\
o_2&=(T+c, T+\{q,\gamma,c\},
             T+\{\gamma,c\}, T+\{q,c\}).          \tag{1.3}
\end{aligned}

Replace `o_1,o_2,e` by

\[
\begin{aligned}
n_1&=(T+\delta, L+\{\gamma,\delta\},
                  T+\{\gamma,\delta\}, L+\delta),\\
n_2&=(T+c, T+\{\gamma,\delta,c\},
             T+\{\gamma,c\}, T+\{\delta,c\}),\\
n_3&=(L, T+\{q,\gamma,c\},
          L+\gamma, T+\{q,c\}).                  \tag{1.4}
\end{aligned}

Direct intersection, union, tail, and head comparison gives

\[
             \operatorname{res}\{o_1,o_2,e\}
             =\operatorname{res}\{n_1,n_2,n_3\}.   \tag{1.5}
\]

## 2. Exact forest theorem

### Theorem 2.1

Start with the old three-socket table and the two isolated directed edges
`o_1,o_2`.  Apply the three fibre `C10` switches, the first Boolean `C6`
fusion, and then (1.3)--(1.4).  The topology is

\[
 15C_4+2K_2\ \longrightarrow\ 3C_{20}+2K_2
 \ \longrightarrow\ C_{60}+2K_2
 \ \longrightarrow\ P_{62}+P_2.                  \tag{2.1}
\]

Both banks remain matchings; all 62 lower, upper, tail, and head resources
are pairwise distinct; and the complete old/new four-row multisets agree
literally.  Thus the final table is a forest with no palette defect.

#### Proof

Only `e` overlaps the old socket table.  Every other resource in (1.3)
contains the fresh coordinate `c`, except `T+delta` and
`T+{gamma,delta}`.  Their `H` cores omit `q` and contain respectively two
and three displayed markers, so they differ from every horizontal or
vertical socket core.  Hence `o_1,o_2` are two isolated matching edges and
all new non-target resources are likewise exterior.

Deleting `e` opens the `C60`; deleting `o_1,o_2` opens the two isolated
edges.  The new Boolean-hex matching reconnects their six endpoints in the
standard cycle-opening mode, giving two paths.  There are 64 vertices and
62 edges, and direct tracing gives component sizes `62` and `2`.
Equation (1.5) proves exact four-row preservation, while distinctness of
the six endpoints proves the second-bank matching row.  The first bank is
unchanged after the three already-audited `C10` switches.  QED.

The complete replacement has 21 old and 21 new atoms: fifteen from the
three `C10` moves, three from the fusion `C6`, and three from the opening
`C6`.

## 3. Audit

The same lightweight verifier as the core theorem checks (2.1) and all
literal resources for every `6<=m<=20`:

```text
scratch/a_three_socket_c10_c6_fusion_20260802/
  audit_a_three_socket_c10_c6_fusion_20260802.py
```
