# The voltage-two path anatomy and the local packet invariant suggested for \(m=5\)

Date: 2026-07-31  
Status: exact path/closure theorem for the authenticated \(m=4\) fixture;
exact obstruction to a global \(\mathbb Z_9\) analogue; conditional local
packet target for \(m=5\), not an \(m=5\) construction

## 1. The two quotient paths

Identify the old coordinates with

\[
[8]=\mathbb Z_7\sqcup\{\infty\},
\]

where bit `0x80` is \(\infty\), and let \(\rho\) add one on the finite
coordinates.  In the canonical oriented forest, take the path representatives

```text
S = aa,8e,0f
L = 1d,17,56,66,e4,b4,b1.
```

The fourteen paths, in physical closure order, are exactly

\[
S_t=\rho^{2t}S,\qquad L_t=\rho^{2t}L,qquad
S_0,L_0,S_1,L_1,\ldots,S_6,L_6.                 \tag{1.1}
\]

Thus the short and long paths are the two free \(\mathbb Z_7\)-orbits.
Their quotient forest consists of paths of sizes three and seven.  Its two
closure-edge orbits are

\[
 e_t=(\operatorname{end}S_t,\operatorname{start}L_t),qquad
 k_t=(\operatorname{end}L_t,\operatorname{start}S_{t+1}). \tag{1.2}
\]

Adding them makes a quotient ten-cycle.  One trip around that quotient
advances the finite coordinates by two, so the physical cycle is its
voltage-\(2\) lift.  Since \(\gcd(2,7)=1\), it is connected.  Equivalently,
rotation by one sends path-pair index \(t\) to \(t+4\), hence advances the
70-cycle by \(4(3+7)=40\) positions.  After suppressing the two path tails,
the same calculation advances the 56-cycle by \(4(2+6)=32\) positions.

## 2. The seven forced ears in path language

At every \(S_t\to L_t\) junction, suppressing the long-path tail gives the
repair triple

\[
 E_t=(O_t,D_t,Z_t)=
 \bigl(L_t(0),\ \operatorname{end}S_t\cap L_t(1),\
 L_t(0)\cap L_t(1)\bigr).                              \tag{2.1}
\]

These are exactly the seven forced ears.  In raw mask notation:

| \(t\) | \(\rho\)-power | short path | long path | closure | \((O,D,Z)\) |
|---:|---:|---|---|---|---|
| 0 | 0 | `aa,8e,0f` | `1d,17,56,66,e4,b4,b1` | `0f->1d` | `(1d,07,15)` |
| 1 | 2 | `a9,b8,3c` | `74,5c,5a,1b,93,d1,c5` | `3c->74` | `(74,1c,54)` |
| 2 | 4 | `a5,e1,71` | `53,72,6a,6c,cc,c6,96` | `71->53` | `(53,70,52)` |
| 3 | 6 | `95,87,47` | `4e,4b,2b,33,b2,9a,d8` | `47->4e` | `(4e,43,4a)` |
| 4 | 1 | `d4,9c,1e` | `3a,2e,2d,4d,c9,e8,e2` | `1e->3a` | `(3a,0e,2a)` |
| 5 | 3 | `d2,f0,78` | `69,39,35,36,a6,a3,8b` | `78->69` | `(69,38,29)` |
| 6 | 5 | `ca,c3,63` | `27,65,55,59,99,8d,ac` | `63->27` | `(27,61,25)` |

The first row is the representative `(29,7,21)` of the orbit
\(\mathcal E\) in
`MATH_THEOREM_CATALAN_M4_Z7_QUOTIENT_REPAIR_CORE_20260731.md`.
Every long tail avoids \(\infty\).  Literal reconstruction of the complete
core shows that its omitted token, base and outgoing colour all have degree
one, so (2.1) is forced on every rotation.

## 3. The two kernel edge orbits

At the other closure junction, \(L_t\to S_{t+1}\), suppression of the short
tail gives

\[
 K^0_t=\bigl(S_{t+1}(0),\ \operatorname{end}L_t\cap S_{t+1}(1),\
 S_{t+1}(0)\cap S_{t+1}(1)\bigr).                      \tag{3.1}
\]

This is the selected kernel orbit.  The same short-tail token and outgoing
colour have exactly one other viable host: the terminal internal edge of
\(L_{t-1}\).  It gives

\[
 K^1_t=\bigl(S_{t+1}(0),\ L_{t-1}(5)\cap L_{t-1}(6),\
 S_{t+1}(0)\cap L_{t-1}(6)\bigr).                      \tag{3.2}
\]

The seven instances of (3.1) and (3.2) are the two residual kernel orbits
\(\mathcal K_0,\mathcal K_1\).  Thus the three core orbits have a direct
path interpretation:

```text
E   = short-to-long closure orbit;
K0  = long-to-next-short closure orbit;
K1  = alternate host at the previous long path's terminal forest edge.
```

No other duplicated-base/hole-compatible host survives.  The complete core
is therefore \(\mathcal E\sqcup\mathcal K_0\sqcup\mathcal K_1\), while the
canonical matching is \(\mathcal E\sqcup\mathcal K_0\).  Quotienting turns
the seven forced ears into one forced edge and the residual 14-cycle into
one binary pair of parallel edges.

## 4. The dimension-independent local invariant

The part which can sensibly recurse is not global cyclic symmetry.  It is
the following **ear--binary-cycle packet**.

1. The occurrence core splits into forced ear edges and a residual shore.
2. On the residual shore there are two perfect matchings \(K_0,K_1\).
3. The transition permutation \(K_0^{-1}K_1\) is one cycle inside each
   packet.
4. The physical path closure realizes the forced edges and \(K_0\) by two
   protected junction types; every \(K_1\) edge is supplied by a protected
   internal host, and there are no further core edges.

For one packet the perfect matching is forced on the ear shore and has one
binary choice on the kernel shore.  A disjoint union of \(c\) packets has
exactly \(2^c\) repairs.  This formulation retains the useful quotient bit
without requiring a transitive coordinate group or a leaf-peelable core.

## 5. Why the global \(\mathbb Z_7\) quotient cannot become a global
\(\mathbb Z_9\) quotient

For \(m=5\), write the ten coordinates as
\(\mathbb Z_9\sqcup\{\infty\}\).  Every rank-five set has a free
\(\mathbb Z_9\)-orbit.  Indeed a nontrivial stabilizer contains the unique
order-three subgroup.  Its finite-coordinate orbits have size three, so an
invariant set has a number of finite coordinates divisible by three.  A
rank-five set has five finite coordinates when it avoids \(\infty\), and
four when it contains \(\infty\); neither is divisible by three.

Consequently every \(\mathbb Z_9\)-invariant collection of middle facets has
cardinality divisible by nine.  But

\[
K_5=\operatorname{Cat}_5=42\not\equiv0\pmod 9.        \tag{5.1}
\]

Hence no \(m=5\) saturating cycle can have a globally
\(\mathbb Z_9\)-invariant Catalan leave of size 42.  The exact three-free-
orbit theorem at \(m=4\) therefore cannot recurse verbatim.

## 6. The exact ternary packet ledger at \(m=5\)

There is nevertheless a dimension-specific local ledger:

\[
(M_4,N_4,K_4)=(70,56,14),\qquad
(M_5,N_5,K_5)=(252,210,42),                              \tag{6.1}
\]

and

\[
K_5=3K_4,qquad M_5=3M_4+K_5,qquad N_5=3N_4+K_5.       \tag{6.2}
\]

Thus three copies of the authenticated \(m=4\) path packet have 210 middle
vertices, 168 internal edges and 42 path components.  Extending every path
by one fresh vertex and one fresh lower/upper flag gives exactly

\[
252\text{ vertices},\qquad210\text{ edges},\qquad42\text{ paths},
\]

which are the forced \(m=5\) forest counts.  The path-size forecast is
\(4^{21}8^{21}\).  On the repair side, three packet cores would have

\[
42\text{ selected repairs},\quad63\text{ complete-core edges},\quad
21\text{ forced ears},\quad3\text{ binary kernels},
\]

and hence eight perfect matchings.

This is the smallest local invariant consistent with both the voltage-two
fixture and the exact Catalan/Pascal counts.  It becomes an \(m=5\)
construction only if one also proves all of the following physical gates:

* three colour-disjoint packet embeddings plus 42 extension flags cover
  every rank-four and rank-six colour exactly once;
* the extensions and inter-packet splices create no extra repair-core edge;
* the 42 paths admit one equal-union Hamilton closure whose local junctions
  retain the ear and selected-kernel hosts; and
* protected splicing joins the three packet cycles without destroying the
  upper, residence or compiler invariants.

None of these physical existence claims follows from the arithmetic.  The
result is an exact recursive target and an exact obstruction to the more
naive global-cyclic target.

There is a further exact scope correction from the three-primary quotient
theorem.  At \(m=5\),

\[
q=9,\qquad s=3^{v_3(q)}=9,\qquad h=q/s=1.
\]

Therefore the three copies in (6.2) are **not** the theorem's nine residual
braid sectors.  Their factor three is only the displayed Pascal/count
identity.  Since \(h=1\), equivariance is vacuous; neither a nine-sector
braid nor an aggregation of its sectors into these three modules is
constructed here.  The packet conclusion is valid only conditionally on
the stated label separation and absence of cross-packet repair triples.

## 7. Reproduction and scope

The path and orbit assertions are independently replayed by the audit
`scratch/audit_catalan_m4_path_closure_m5_packet_ledger_20260731.py`.
The \(m=5\) checks are finite orbit and binomial identities.  No SAT search,
\(m=5\) carrier or all-dimensional induction is claimed.
