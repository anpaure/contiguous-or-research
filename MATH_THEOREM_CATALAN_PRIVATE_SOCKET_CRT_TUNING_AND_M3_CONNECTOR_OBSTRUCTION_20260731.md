# Private socket CRT tuning and the first transparent connector obstruction

Date: 2026-07-31  
Status: exact cyclic-group tuning law; explicit smallest transparent
connector-transport obstruction in the frozen `m=2,3,4` fixtures; no
all-`m` private-socket existence claim

## 0. Verdict

Fix a one-cycle occurrence closure for a free action
\(H\cong\mathbb Z_h\).  Suppose some connector sockets are private and each
may be replaced independently by a parallel connector with the same
oriented endpoint occurrences.  If their gain menus are
\(G_1,\ldots,G_k\subseteq\mathbb Z_h\), absorb orientation signs into the
menus and put

\[
                         S=G_1+\cdots+G_k.             \tag{0.1}
\]

The weakest condition which makes the total voltage primitive for **every**
base voltage is

\[
             \boxed{\ U_h-S=\mathbb Z_h\ }
             \qquad\Longleftrightarrow\qquad
             \boxed{\ S+U_h=\mathbb Z_h\ },           \tag{0.2}
\]

where \(U_h=\{u:\gcd(u,h)=1\}\).  In CRT coordinates this says that, for
every choice of one forbidden residue \(a_p\in\mathbb F_p\) at each prime
\(p\mid h\), some \(s\in S\) avoids all of them simultaneously:

\[
                       s\not\equiv a_p\pmod p
                       \quad\hbox{for every }p\mid h. \tag{0.3}
\]

Only the image of \(S\) modulo \(\operatorname{rad}(h)\) matters.

There is a sharp prime-power/mixed-prime distinction.

* If \(h=p^a\), (0.2) holds exactly when \(S\bmod p\) has at least two
  elements.  Thus one private binary socket is a universal tuner exactly
  when its two gains differ nontrivially modulo \(p\).
* If \(h\) has at least two distinct prime divisors, no two-element \(S\)
  is a universal tuner, even when its difference is a unit and generates
  \(\mathbb Z_h\).  For example, at \(h=6\), \(S=\{0,1\}\) fails at base
  voltage \(2\), since the two totals are \(2\) and \(3\).

The topology gate remains earlier than this arithmetic law.  The first
transparent connector-transport failure is already at `m=3`, not `m=4`.
A fixed common connector matching closes one side of an exact transparent
split to a `20`-cycle and the other side to cycles `9+11`.  The `m=4`
example frozen in item 2170 is only the first such failure with both
middle-level factors Hamiltonian.

## 1. Exact private-gain law

### Theorem 1.1 (universal primitive tuner)

Assume that all choices in the private menus retain the same literal
connector matching, endpoint pairing and one-cycle occurrence topology.
Let \(v\in\mathbb Z_h\) be the total gain of every fixed path and connector
fragment.  The attainable closed voltages are

\[
                              v+S.                    \tag{1.1}
\]

The following are equivalent.

1. For every \(v\in\mathbb Z_h\), some element of \(v+S\) is primitive.
2. \(U_h-S=\mathbb Z_h\).
3. \(S+U_h=\mathbb Z_h\).
4. For every tuple \((a_p)_{p\mid h}\), there is \(s\in S\) satisfying
   (0.3).
5. No translate of \(S\) is contained in the non-generators of
   \(\mathbb Z_h\).

#### Proof

The equation \(v+s=u\in U_h\) is equivalent to \(v=u-s\), proving `1 <=> 2`.
Negate the equality and use \(-U_h=U_h\) to obtain `2 <=> 3`.  A residue is
a unit modulo \(h\) exactly when it is nonzero modulo every prime divisor of
\(h\).  With \(a_p=-v\bmod p\), this gives `1 <=> 4`.  Negating the unit
intersection statement gives `1 <=> 5`.  The same CRT statement shows that
prime-power exponents are irrelevant.  \(\square\)

The word **private** is substantive here: it makes the choices independent,
so their attainable gain set is the Minkowski sum (0.1).  If two alternatives
compete for a literal resource, change the endpoint occurrence, or alter the
path pairing, (1.1) is not the correct state.

### Corollary 1.2 (prime powers)

For \(h=p^a>1\), a sumset \(S\) is a universal tuner if and only if

\[
                              |S\bmod p|\ge2.          \tag{1.2}
\]

Indeed, one forbidden residue covers \(S\bmod p\) exactly when that image is
a singleton.  Composite prime powers therefore behave like primes here.

### Corollary 1.3 (mixed-prime two-value no-go)

If \(\omega(h)\ge2\), no set \(S=\{s,t\}\) is a universal tuner.

#### Proof

Choose different primes \(p,q\mid h\).  CRT supplies a base \(v\) with

\[
                         v\equiv-s\pmod p,
                         \qquad v\equiv-t\pmod q.     \tag{1.3}
\]

Then \(v+s\) is divisible by \(p\), while \(v+t\) is divisible by \(q\).
Neither total is primitive.  \(\square\)

More generally, any \(S\) with \(|S|\le\omega(h)\) fails: assign a different
prime to every element of \(S\), prescribe the killing congruence at that
prime, and apply CRT.  The converse cardinality statement is false.  At
\(h=30\), the four-element set

\[
                              S=\{2,3,5,6\}            \tag{1.4}
\]

has at least two residues modulo each of \(2,3,5\), yet base \(v=0\) kills
every choice.  Separate nonconstant prime projections, a unit difference,
and generation of the ambient group are all weaker than (0.3).

The finite audit finds the smallest menu sizes `4,3,6` for
\(h=6,15,30\), with witnesses respectively

\[
                 \{0,1,2,3\},\qquad
                 \{0,1,2\},\qquad
                 \{0,1,2,3,4,5\}.                   \tag{1.5}
\]

These are calibrations, not a claimed closed formula for arbitrary \(h\).

### Corollary 1.4 (CRT-separated private face)

For every prime \(p\mid h\), choose a private binary socket with gain
difference \(\delta_p\) satisfying

\[
 \delta_p\not\equiv0\pmod p,
 \qquad
 \delta_p\equiv0\pmod q\quad(q\mid h,\ q\ne p).     \tag{1.6}
\]

Then the independent menus \(\{0,\delta_p\}\) form a universal tuner.

#### Proof

In the \(p\)-coordinate, all knobs except the \(p\)-knob are constant.  If
the current total is already nonzero modulo \(p\), select `0`; otherwise
select \(\delta_p\).  These coordinatewise choices are independent and
make the final total nonzero at every prime.  \(\square\)

This gives a clean positive private-socket face with one binary knob per
distinct prime.  It is sufficient, not weakest: the exact weakest law is
(0.2)--(0.3).  For example, at \(h=6\), two identical binary menus
\(\{0,1\}\) have sumset \(\{0,1,2\}\) and still fail at base `2`, whereas
three such menus have sumset \(\{0,1,2,3\}\) and succeed.

For a tree boundary state, an oriented internal path fragment carries a
gain \(g\), reversal carries \(-g\), and serial gluing adds gains.  A private
parallel socket replaces a singleton gain by its menu, so composition is
Minkowski addition of subsets of \(\mathbb Z_h\).  Thus the exact
group-valued coordinate is finite for fixed \(h\).  It must be indexed by
the physical boundary pairing; an anonymous socket multiplicity does not
determine which gains lie on which eventual cycle.

## 2. Smallest transparent topology obstruction

### Proposition 2.1 (`m=2` has no transition)

The frozen `ML(3)` fixture is its unique six-cycle.  Its only incidence
hexagon is the whole graph, so the cycle contains all six hexagon edges,
not one alternating matching with the other matching absent.  Hence it has
zero standard alternating incidence-hexagon toggles.  There is no `m=2`
connector-transport transition to test.

### Proposition 2.2 (literal `m=3` failure)

Take the frozen middle-levels Hamilton cycle

```text
3 7 5 13 9 11 10 26 24 25 17 21 20 28 12 14 6 22 18 19
```

and the common decoration

\[
 D_A=\{3,9,12,17,24\},\qquad
 D_B=\{11,13,19,25,28\}.                            \tag{2.1}
\]

Toggle \(H=1,(a,b,c)=(1,3,4)\):

\[
 \{(3,19),(9,11),(17,25)\}
 \longrightarrow
 \{(3,11),(9,25),(17,19)\}.                         \tag{2.2}
\]

All six hexagon vertices are marked.  The selected local upper palette is
\(\{15,23,29\}\), the selected local lower palette is \(\{2,8,16\}\) on
both sides, and the retained-fragment boundary types alternate after
reconnection.  Thus (2.2) is transparent for (2.1).  The new middle-level
factor has two cycles of order `10`, but both sides lift to five physical
paths in \(J(6,3)\) and have identical degree deficits at every vertex.

Their endpoint-pairing involutions are

\[
\begin{split}
P_0={}&(11\ 13)(19\ 44)(22\ 35)(28\ 38)(49\ 56),\\
P_1={}&(11\ 56)(13\ 35)(19\ 44)(22\ 49)(28\ 38).   \tag{2.3}
\end{split}
\]

Thus the relative endpoint permutation is

\[
                  P_1P_0=(11\ 35\ 49)(13\ 56\ 22), \tag{2.4}
\]

fixing `19,28,38,44`.  This is the exact local three-break which socket
multiplicity misses.

Now use the common literal connector set

\[
 M=\{(11,19),(13,28),(22,38),(35,49),(44,56)\}.     \tag{2.5}
\]

Every member is a distinct Johnson edge, avoids both forests, and uses every
endpoint once.  The old occurrence graph \(P_0\cup M\) is one `10`-port
cycle, and its physical realization is the `20`-cycle

```text
7 19 11 13 28 14 38 22 50 35 49 56 44 52 21 25 26 42 41 37
```

The new occurrence graph \(P_1\cup M\) has port-cycle orders `4+6`, and its
physical realization has cycles

```text
7 11 19 21 52 44 56 41 37
13 25 26 42 35 49 50 22 38 14 28
```

of orders `9+11`.  Hence decoration transparency, equal socket
multiplicities and one unchanged legal connector matching do not transport
occurrence connectivity.

The common endpoint catalogue has 15 legal candidate edges and exactly four
perfect matchings.  Their complete closure census is

\[
\begin{array}{c|c|c}
\text{old physical orders}&\text{new physical orders}&\#\\ \hline
20&20&1\\
20&9+11&1\\
8+12&20&2.
\end{array}                                          \tag{2.6}
\]

Thus the witness is not caused by an incomplete connector search.

### Corollary 2.3 (minimality and the `m=4` comparison)

Among the frozen `m=2,3,4` fixtures, Proposition 2.1 and Proposition 2.2 make
`m=3` the smallest transparent connector-transport obstruction.  If both
the pre- and post-toggle middle-level factors are required to be Hamilton
cycles, `m=4` is first.  In item 2170's `H=20,(1,3,5)` example, the affected
endpoint pairs change as

\[
\begin{split}
 &(46\ 53)(60\ 139)(90\ 165)\\
 &\hspace{12mm}\longrightarrow
   (46\ 165)(53\ 60)(90\ 139),                     \tag{2.7}
\end{split}
\]

whose relative product is

\[
                     (46\ 60\ 90)(53\ 165\ 139).   \tag{2.8}
\]

The frozen connector set closes the old forest to `70` and the new one to
`46+24`.

No voltage choice can repair a failure such as `9+11` or `46+24` while the
pairing and connector topology are fixed: the quotient already has at least
two occurrence cycles.  Primitive tuning applies only after the one-cycle
topology gate passes.

## 3. Audit

Run

```text
python3 scratch/audit_catalan_private_socket_crt_tuning_m3_connector_obstruction_20260731.py
```

The replay exhausts the CRT equivalence on every gain subset for
`2 <= h <= 12`, exhausts the prime-power specialization on the displayed
small prime powers, checks every two-element set for all mixed-prime
`h <= 60`, verifies the sharp small examples and CRT-separated construction,
and independently reconstructs the complete `m=3` connector census.

Audit output:

```text
scratch/catalan_private_socket_crt_tuning_m3_connector_obstruction_20260731.audit.json
```

Canonical payload SHA-256:

```text
34b059ec776b661a6380f359d433398ba863abd665a3cbbf22cd1ee24fa15df6
```
