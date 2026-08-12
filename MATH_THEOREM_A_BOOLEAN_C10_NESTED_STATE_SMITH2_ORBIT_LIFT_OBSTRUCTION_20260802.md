# Boolean `C10` nested-state Smith-2 orbit-lift obstruction

**Date:** 2026-08-02  
**Lane:** A, integral rotor fusion  
**Status:** exact finite counterexample for a restricted K11 decorated-row
submaster.  It is **not** a no-go for the full K11 ideal, K19, K21, or an
enlarged state catalogue.

## 0. Verdict

There is a five-row K11 Boolean catalogue with all of the following
properties.

1. Every row is a strict rank-4 to rank-5 chain carried by the strictly
   nested contiguous addresses `12 < 123`, and has a rank-6 owner.
2. Every physical row has two nonempty literal three-cell states.
3. The exact literal compatibility digraph on the ten states is one
   directed `C10`.
4. Weight `1/2` on every state and every directed edge is a balanced
   fractional solution covering every chain target and owner once.
5. The cyclic symmetry has one state orbit, one arc orbit, and integral
   orbit totals equal to five.
6. No integral balanced selection exists.  The reduced constraint matrix
   has Smith normal form

   \[
                         \operatorname{diag}(1^9,2).       \tag{0.1}
   \]

Thus even a literal Boolean nested-chain catalogue, a complete primitive
circuit, and integral orbit totals do not imply an integral orbit lift.
The obstruction is an exact `Z/2` resource-image residue, not missing
reset capacity.

## 1. The five physical rows

Work in `[11]`.  Use active coordinates

\[
                 a_0,a_1,a_2,a_3,a_4,g_0,g_1,          \tag{1.1}
\]

and leave the other four coordinates unused.  Subscripts on the `a`'s are
modulo five, and put, for `t` modulo ten,

\[
                 c_t=\{a_{t\bmod5},g_{t\bmod2}\}.       \tag{1.2}
\]

The ten cells are nonempty and pairwise distinct.  For `i` modulo five,
define

\[
\begin{aligned}
 C_i&=\{a_i,a_{i+1},g_0,g_1\},\\
 U_i&=\{a_i,a_{i+1},a_{i+2},g_0,g_1\},\\
 T_i&=U_i\cup\{a_{i-1}\}.
\end{aligned}                                           \tag{1.3}
\]

Hence

\[
                    |C_i|=4,\qquad |U_i|=5,\qquad |T_i|=6, \tag{1.4}
\]

and the five sets in each of the three families are pairwise distinct.
Physical row `i` is the strict chain

\[
                              C_i\subset U_i             \tag{1.5}
\]

with owner `T_i`.

For `t` modulo ten, let `q_t` be the decorated state

\[
                 q_t=(c_t,c_{t+1},c_{t+2}),qquad i=t\bmod5. \tag{1.6}
\]

Every cell is nonempty, and direct union gives

\[
                 c_t\cup c_{t+1}=C_i,qquad
                 c_t\cup c_{t+1}\cup c_{t+2}=U_i.       \tag{1.7}
\]

Thus `q_t` realizes (1.5) on the strict nested address chain

\[
                                  12\subset123.          \tag{1.8}
\]

Because adding five reverses parity without changing the `a`-subscript,

\[
                       q_i,\ q_{i+5}                     \tag{1.9}
\]

are two different literal states of the same physical row, with the same
two targets and the same owner.

## 2. Exact compatibility is one directed `C10`

Use the literal shift-and-owner rule

\[
 q_t\longrightarrow q_s
 \quad\Longleftrightarrow\quad
 (q_t)_2=(q_s)_1,quad (q_t)_3=(q_s)_2,quad
 (q_t)_1\cup U_{s\bmod5}=T_{s\bmod5}.               \tag{2.1}
\]

### Theorem 2.1 (exact successor graph)

Among the ten states,

\[
                    q_t\longrightarrow q_s
                    \quad\Longleftrightarrow\quad
                    s=t+1\pmod {10}.                  \tag{2.2}
\]

#### Proof

The cells `c_t` are pairwise distinct.  The two retained-cell equalities
in (2.1) therefore force `s=t+1`.  Conversely, for this value of `s`, the
two shift equalities are tautological, and

\[
 c_t\cup U_{t+1}
 =U_{t+1}\cup\{a_t\}=T_{t+1};                       \tag{2.3}
\]

the phase coordinate in `c_t` is already in `U_(t+1)`.  Hence every
successor edge is legal and there are no others.  \(\square\)

## 3. Fractional feasibility and integral impossibility

Let `y_t` select state `q_t`, and let `x_t` select its unique outgoing edge
`q_t -> q_(t+1)`.  Exact use of physical row `i` gives

\[
                             y_i+y_{i+5}=1.             \tag{3.1}
\]

This single equation simultaneously enforces the unique uses of `C_i`,
`U_i`, and `T_i`.  State balance on the directed `C10` gives

\[
                         x_t=y_t=x_{t-1}.              \tag{3.2}
\]

### Theorem 3.1 (Smith-2 obstruction)

The fractional assignment

\[
                         y_t=x_t={1\over2}quad(t\in\mathbb Z_{10}) \tag{3.3}
\]

is feasible, but (3.1)--(3.2) have no integral solution.

#### Proof

Equation (3.2) makes all ten `y_t` equal to one common value `c`.
Equation (3.1) then reads

\[
                                  2c=1,                \tag{3.4}
\]

whose unique rational solution is `c=1/2` and which has no integral
solution.  Equivalently, all `2^5=32` binary choices of one phase per
physical row violate circulation balance.  \(\square\)

There is a literal determinant certificate.  Take the nine independent
balance rows

\[
                          y_t-y_{t+1}=0\quad(0\le t<9) \tag{3.5}
\]

and the resource row `y_0+y_5=1`.  Their `10 x 10` coefficient matrix has
determinant `2`.  The first nine rows restricted to columns zero through
eight form a determinant-one minor.  Therefore the Smith invariants are
exactly (0.1).  Modulo two, the sum of balance rows zero through four and
the resource row has zero left side and right side one.  This is an
explicit `Z/2` Farkas certificate.

## 4. The orbit totals are integral

Let

\[
                 R=(a_0\ a_1\ a_2\ a_3\ a_4)(g_0\ g_1), \tag{4.1}
\]

fixing the four unused coordinates.  Then

\[
                 R(c_t)=c_{t+1},\qquad R(q_t)=q_{t+1}. \tag{4.2}
\]

Thus the ten configurations form one `R`-orbit, the ten directed arcs form
one `R`-orbit, and each of the `C`, `U`, and `T` resource families forms one
five-element orbit.  Under (3.3), the configuration-orbit total and the
arc-orbit total are both

\[
                               10\cdot{1\over2}=5.      \tag{4.3}
\]

They are integers and give the correct total demand five on every resource
orbit.  Nevertheless Theorem 3.1 proves that the orbit solution has no
literal integral lift.

The cyclic group generated by `R` preserves the two-coordinate set
`{g_0,g_1}` and is a subgroup of a fixed-core stabilizer.  The theorem is
about this invariant restricted catalogue.  Taking the full stabilizer
orbit closure would add configurations and is not covered by the no-go.

## 5. Circuit completeness, Smith residues, and normality

The compatibility graph already has its complete primitive directed-cycle
catalogue: it consists of the one `C10`.  Its physical resource vector is

\[
                              (2,2,2,2,2),             \tag{5.1}
\]

because the cycle uses both phases of every row.  The demand vector is
`(1,1,1,1,1)`, which is outside the integer image lattice by Theorem 3.1.
Hence circuit or Markov-basis completeness alone cannot prove existence.

More generally, freeze a finite state digraph and let the columns of
`Z` be its primitive integral circulation circuits.  Let `A` record the
physical target/owner uses.  Every integral balanced selection has resource
vector

\[
                                  AZ\lambda,qquad
                                  \lambda\in\mathbb Z_{\ge0}. \tag{5.2}
\]

Thus Smith congruences for the lattice generated by the columns of `AZ`
are unavoidable.  If, in addition, the nonnegative column semigroup of
`AZ` is normal and the required box/capacity bounds are respected, then
cone feasibility plus those Smith congruences is sufficient.  Without
normality, lattice membership still need not imply nonnegative integral
membership; circuit completeness only connects an already nonempty fibre.

This is the proof-safe sense in which the Smith residue is the only
obstruction under a **normal circuit-image semigroup**.  Circuit
completeness by itself is weaker.

## 6. Reset capacity and the K19/K21 scope

All five physical rows here have length two.  There are no long flags, so

\[
                             D=(0,0,0),\qquad \rho(D)=0. \tag{6.1}
\]

The raw short-row budget is maximal, yet the integral state lift fails.
Consequently the K19 and K21 bounds

\[
\begin{aligned}
 14976&\le N_{\rm short}\le14991 &&(K19),\\
 8736&\le N_{\rm short}\le9573  &&(K21)
\end{aligned}                                           \tag{6.2}
\]

cannot by themselves remove an orbit-lattice obstruction.  After the
fixed-core fractional master and the monotone reset cuts pass, one must
still test the Smith lattice of the circulation-to-resource map, or plant
a macro whose resource vector generates the missing residue class.

For this gadget, opening the `C10` and retaining any five consecutive
states produces a directed path using every physical row once.  Thus one
compatible external predecessor and one compatible external successor are
an exact parity-breaking absorber.  Their Boolean existence is not supplied
by the raw count of short rows.

Finally, this obstruction is compatible with a critical or maximal K11
interval-packing theorem, including the Dong--Mao result: the five chains
(1.5) are already legitimate strictly nested Boolean intervals.  The
failure occurs only after this restricted catalogue also fixes the two
literal phase states and demands balanced chronology.  It does not refute
another interval packing, another state catalogue, or the full K11 joint
master.

## 7. Exact replay

The independent verifier

```text
scratch/audit_a_boolean_c10_nested_state_smith2_20260802.py
```

checks all ranks, strict containments, cell nonemptiness, the address
identities, all `10^2` possible literal arcs, the fractional loads, all 32
binary resource selections, the symmetry orbits, the determinant-two and
unit-minor certificates, and the explicit mod-two contradiction.  Its
payload is frozen at

```text
scratch/a_boolean_c10_nested_state_smith2_20260802.audit.json
```

with hashes

```text
verifier    eaf17c8d1f25bd70de2b9215efeb5f6d40a5c9ef61efe7fb67eb5291f52daa15
audit JSON  80e385ef21f288ab6c6ebdb220e0a5ee8bf273555b0e9d1532d70ff20a1157fd
```

