# Independent audit: correlated C6 endpoint/socket routing

Date: 2026-07-31  
Lane: AD independent proof audit  
Audited theorem:
`MATH_THEOREM_AD_CORRELATED_C6_ENDPOINT_PERMUTATION_AND_CLOSED_SOCKET_ROUTING_20260731.md`  
Audited SHA-256:
`5dad39291ab56187cd56efec0ac84e6cb452ee8e5a07fc0e8b2ab20355eeeec5`

## 1. Verdict

**PASS at the stated conditional scope.**  Two independent adversarial
reads checked the endpoint-permutation, group/voltage, rooted-graphic,
outer-pairing, slot, Catalan-scale and common-cap arguments.  The audit made
the following scope corrections before the hash above was frozen.

1. Socket-graph connectivity controls only the permutation projection.
   Exact routing is joint reachability in endpoint action, outer-pairing
   action when protected, and literal slot voltage.
2. A precompletion socket must satisfy an explicit decoder-equivariance
   square; it is not enough to name its action before C6 decoding.
3. The physical test uses the actual net old and terminal rooted states.
   Transient atoms in a serialized word are not counted twice.
4. The complete postcompletion composite, not each constituent socket, must
   pass one joint rooted fundamental-cycle/cap test.
5. The `n>=3b+1` private-support bound is a uniform sufficient scalar
   condition, not a necessary sharp threshold for packets of size at most
   `b`.
6. The 203/2430 boundary-partition state is minimal for arbitrary port-graph
   attachments; a restricted Boolean catalogue may admit a quotient of that
   state.
7. Sparse cycles preserve the two outer resource sets, but may change their
   lower-to-upper pairing and hence a pointwise cap map.

No finite search, SAT call, or web input is used in the theorem or this
audit.

## 2. Decisive checks

### 2.1 Endpoint permutation

After deleting one reset arc `t_i -> s_i` for every label, the no-reset-cycle
hypothesis leaves directed paths from the starts to the terminals.  Their
endpoint map is a permutation.  Following a reset after a physical path
applies this permutation, so augmented cycles and permutation cycles agree
with multiplicity.  Therefore the one-reset row is exactly `sigma=id`.

The minimum unrestricted transposition count is

\[
                         k-c(\sigma),
\]

because a transposition changes cycle count by one.  The pivot-star
factorization reaches this bound.  With left endpoint actions and products
read right-to-left, the physical star order is the reverse of the displayed
factor order, as recorded in the theorem.

### 2.2 Catalan constant

Using

\[
 \operatorname {Cat}_{n+1}
   ={2(2n+1)\over n+2}\operatorname {Cat}_n,
 \qquad
 P={n(n-1)\over n+2}\operatorname {Cat}_n,
\]

one gets exactly

\[
 k=\operatorname {Cat}_{n+1}-\operatorname {Cat}_n
   ={3P\over n-1}.
\]

Thus endpoint correction has `O(P/n)` packet scale.  The old-phase-5 and
old-phase-10 sufficient scalar thresholds `n>=16` and `n>=31` follow from
`3b<=n-1`.

### 2.3 Joint endpoint/slot reachability

For a literal serializable word, the pair `(g_w,d_w)` cannot be separated.
Precompletion requires `(sigma^(-1),b)` and postcompletion requires
`(sigma^(-1),0)` in the actual reachable signature set.  In a reversible,
state-independent atlas this is a subgroup condition.  If `w_0` has the
right endpoint action, the remaining condition is precisely

\[
                         b-d(w_0)\in\Lambda_0,
\]

where `Lambda_0` is the voltage subgroup of identity-action words.

The two-label generator `((12),1)` and its inverse gives the smallest exact
counterexample to separate tests: the socket graph is connected and the
unrestricted voltage lattice is `Z`, but every word with action `(12)` has
odd voltage, so `((12),0)` is unreachable.  The mod-two mixed invariant in
the theorem is therefore valid and necessary in this fixture.

### 2.4 Perfect-state and virtual-rooted normalization

Two perfect matchings on the same typed host have the same all-one incidence
vector.  Subtracting their common part proves that every perfect-to-perfect
packet has zero pointwise displacement.  A single sparse cycle has disjoint
old-only and new-only slot banks, hence cannot act alone after completion.

If `T_I` is the complete leave of `M`, then `M union T_I` is an honest
perfect virtual state, and C6 activation is the balanced exchange

\[
        \bigcup_i(O_i\cup\{T_i\})\longrightarrow\bigcup_iN_i.
\]

Relative to a rooted old tree, the usual binary graphic representation makes
the terminal exchange legal exactly when the fundamental-cycle minor is
nonsingular.  Cancelling common labelled edges between the actual net old
and terminal states avoids the transient-edge double-counting error.

### 2.5 Outer pairing and common cap

A C6 toggle changes the outer pairing by a 3-cycle; a sparse half-length
`ell` toggle changes it by an `ell`-cycle.  Hence C6 plus `ell=5` preserves
pairing parity, while the first authoritative parity-changing sparse case is
`ell=6`, available under `n>=10`.  This outer pairing is distinct from the
endpoint permutation.

Exact outer and slot saturation plus an anchor-capped physical forest gives
the existential local Boolean two-step cap.  It does not fix a prescribed
pointwise cap, extend to global SCDs, or provide the chronological
maximal-envelope compiler.  Tracking the outer-pairing action as a second
permutation coordinate gives the correct protected-cap condition.

### 2.6 Boundary and density counts

The six-port counts are

\[
 B_6=203,qquad
 \sum_j S(6,j)2^j
 =2+124+720+1040+480+64=2430.
\]

For a private target bank of size `T`, choosing a deficiency-`t` lower set
forces its unique upper mate, so there are exactly `binom(T,t)` aligned
ordered pairs.  The uniform-independent and conditionally bank-restricted
probabilities in Proposition 5.1 follow by division by
`binom(P,t)^2` and `binom(T,t)^2`, respectively.

## 3. Exact surviving boundary

The theorem proves a complete **conditional** decoder and routing law.  It
does not supply the all-parameter antecedent.  The first live existence row
is one correlated choice of

* a target-aligned DP/body leave and installed C6 off phases;
* a joint endpoint/outer-pairing/slot signature word;
* a nonsingular rooted terminal exchange;
* two-shore/cumulative-reserve compatibility; and
* a regenerated downstream compiler certificate.

The direct global Joos--Mubayi--Smith route remains closed by its independent
ambient-size/codegree exponent contradiction and is not used here.
